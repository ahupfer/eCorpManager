import requests
from flask import session
from flask_login import current_user, login_user, login_required, logout_user
from . import mining
from app.GetSwaggerData import SwaggerData
from ...models import EveChar


@mining.route('/char', methods=['POST', 'GET'])
@login_required
def char_mining():
    url = 'https://esi.evetech.net/latest/characters/' \
          + str(session['character']['CharacterID']) + '/mining'

    r = SwaggerData


    print r.json()

    return 'char mining'
