from flask import request, redirect, session, url_for
from flask_login import login_required
from app import oauth
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
    print resp
    print (session['character']['CharacterName'])
    return str(session['character'])


# once we've gotten a callback to oauth-response, we can get tokens
# to access the API
@evesso.tokengetter
def get_evesso_oauth_token():
    return session.get('evesso_token')