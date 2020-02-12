from flask.ext.httpauth import httpBasicAuth
from flask import g
from models import User

auth = httpBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    else:
        g.user = user
        return True
    