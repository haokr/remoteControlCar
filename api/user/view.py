from . import user
from flask import abort, request, g
from db import redis_cli
from utils.token import Token


@user.route("/login", methods=["POST"])
def login():
    car_id = g.user.car.id
    user_id = g.user.id
    car_ip = redis_cli.get('car:'+car_id)
    token = Token(user_id, car_ip)
    return token


@user.route("/logout", methods=["POST"])
def logout():
    token = request.args.get('token')
    redis_cli.delete(token)
    return True
