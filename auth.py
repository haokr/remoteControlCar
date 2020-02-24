from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import g, jsonify, request
from models import User
from utils.token import Token
from werkzeug.datastructures import Authorization
import base64


class MyHTTPBasicAuth(HTTPBasicAuth):
    def __init__(self, scheme=None, realm=None):
        super().__init__(scheme, realm)

    def get_auth(self):
        '''使BasicAuth可以自定义scheme
        '''
        auth = None
        if 'Authorization' in request.headers:
            # Flask/Werkzeug do not recognize any authentication types
            # other than Basic or Digest, so here we parse the header by
            # hand
            try:
                auth_type, auth_str = request.headers['Authorization'].split(
                    None, 1)
                username, password = base64.b64decode(auth_str).decode().split(':', 1)
                auth = Authorization(auth_type, {'username': username,
                                               'password': password})
            except ValueError:
                # The Authorization header is either empty or has no token
                pass

        # if the auth type does not match, we act as if there is no auth
        # this is better than failing directly, as it allows the callback
        # to handle special cases, like supporting multiple auth types
        if auth is not None and auth.type.lower() != self.scheme.lower():
            auth = None
        return auth


auth = MyHTTPBasicAuth(scheme="BasicAuth")
token_auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    else:
        g.user = user
        return True


@auth.error_handler
def auth_error():
    return jsonify({"status": "fail"})


@token_auth.verify_token
def verify_token(token):
    token_dict = Token.auth(token)
    if token_dict:
        g.user_id = token_dict.get('user_id')
        g.car_ip = token_dict.get('car_ip')
        g.car_port = token_dict.get('car_port')
        g.token = token
        return True
    else:
        return False

    
