from flask import request, session, url_for, redirect
from flask_login import login_required, current_user
from app import oauth, db
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
    session['character'] = verify.data

# check if EveChar already in the database

    char = EveChar.query.filter_by(character_id = session['character']['CharacterID']).first()

# if not save char into the database in realtion with the current user id

    if char is None:
        char = EveChar(character_id=verify.data['CharacterID'],
                       character_name=verify.data['CharacterName'],
                       character_owner_hash=verify.data['CharacterOwnerHash'],
                       access_token=resp['access_token'],
                       refresh_token=resp['refresh_token'],
                       user_id=current_user.id
                       )
        db.session.add(char)
        db.session.commit()

    return redirect(url_for('main.index'))


# once we've gotten a callback to oauth-response, we can get tokens
# to access the API
@evesso.tokengetter
def get_evesso_oauth_token():
    return session.get('evesso_token')