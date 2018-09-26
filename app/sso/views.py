import requests

from flask import request, session, url_for, redirect
from flask_login import login_required, current_user
from app import oauth, db
from config import Config
from ..models import EveChar
from . import sso


evesso = oauth.remote_app('evesso', app_key='EVESSO')


@sso.route("/login")
@login_required
def login():
    return evesso.authorize(callback=url_for('sso.authorized', _external=True, _scheme="http"))


@sso.route("/authorized")
@login_required
def authorized():
    resp = evesso.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    if isinstance(resp, Exception):
        return 'Access denied: error=%s' % str(resp)

    session['evesso_token'] = (resp['access_token'], '')

    verify = evesso.get('verify')

    # TODO: do we need the access_token and the character in the session variable?

    session['character'] = verify.data
    session['access_token'] = resp['access_token']

    # check if EveChar already in the database

    char = EveChar.query.filter_by(character_id = verify.data['CharacterID']).first()

    # if not save char into the database in relation with the current user id

    if char is None:
        char = EveChar(character_id=verify.data['CharacterID'],
                       character_name=verify.data['CharacterName'],
                       character_owner_hash=verify.data['CharacterOwnerHash'],
                       user_id=current_user.id
                       )
    else:
        char.access_token=resp['access_token']
        char.refresh_token=resp['refresh_token']

    db.session.add(char)
    db.session.commit()

    session['refresh_token'] = resp['refresh_token']

    print resp
    print verify.data
    return redirect(url_for('main.index'))

@sso.route('/refresh')
@login_required
def refresh():
    url = "https://login.eveonline.com/oauth/token"
    r = requests.post(url, {'grant_type': 'refresh_token',
                          'client_id': Config.EVESSO['consumer_key'],
                          'client_secret': Config.EVESSO['consumer_secret'],
                          'refresh_token': session['refresh_token']})
    print r.json()
    return "success"
# "grant_type": "refresh_token", "client_id": "YOUR_CLIENT_ID", "client_secret": "YOUR_CLIENT_SECRET", "refresh_token": "YOUR_REFRESH_TOKEN"


# once we've gotten a callback to oauth-response, we can get tokens
# to access the API
@evesso.tokengetter
def get_evesso_oauth_token():
    return session.get('evesso_token')