import requests
from flask import session
from flask_login import current_user, login_user, login_required, logout_user
from . import mining
from ...models import EveChar


@mining.route('/char', methods=['POST', 'GET'])
@login_required
def show_char_mining():

    url = 'https://esi.evetech.net/latest/characters/' \
          + str(session['character']['CharacterID']) + '/mining'

    r = requests.get(url,{'token':  session['access_token']})

    print r.url

    return 'char mining'
