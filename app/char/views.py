from flask import request, redirect, render_template, flash, url_for
from config import Config

from . import char

@char.route('/login', methods=['POST', 'GET'])
def login():
    client_id = Config.EVE_CLIENT_ID
    redirect_url = Config.EVE_CALLBACK_URL

    # hardcoded for testing propose.
    scope = 'esi-industry.read_character_mining.v1'
    login_server_url = 'login.eveonline.com'
    response_type = 'code'

    eve_logon_URL = 'https://' + login_server_url + '/oauth/authorize?response_type=' + \
        response_type + '&redirect_uri=' + redirect_url + '&client_id=' + client_id + \
        '&scope=' + scope

    return render_template('char/login.html', eve_logon_URL=eve_logon_URL)


@char.route('/callback')
def callback():
    code = request.args.get('code')



