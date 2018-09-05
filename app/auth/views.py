from . import auth


@auth.route('/login', methods=['POST', 'GET'])
def login():
    return "Hello World"