from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import g, jsonify
from models import User
from utils.token import Token

auth = HTTPBasicAuth(scheme="BasicAuth")
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

    
