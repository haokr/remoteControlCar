from . import user
from flask import abort, request, g, jsonify
from db import redis_cli, db
from utils.token import Token
from auth import auth, token_auth
from models import User


@user.route("/login", methods=["POST"])
@auth.login_required
def login():
    car = g.user.car
    token = None
    car_ip_port = ''
    user_id = g.user.id
    car_id = ''
    if car:
        car_id = car.id
        car_ip_port = redis_cli.get('car:'+car_id)
    if not car_ip_port:
        token = Token(user_id)
    else:
        car_ip,car_port = car_ip_port.split(":")
        token = Token(user_id, car_id, car_ip, car_port)
    return jsonify({'status': 'success', 'data': token.get()})


@token_auth.login_required
@user.route("/logout", methods=["POST"])
def logout():
    token = g.token
    keys = redis_cli.keys(f'token:{token}:*:*')
    if keys:
        redis_cli.delete(keys[0])
    return jsonify({'status': 'success'})


@user.route("/logon", methods=["POST"])
def logon():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User(username=username)
    user.hash_password(password)
    
    db.session.add(user) 
    db.session.commit()
    return jsonify({'status': 'success', 'data': user.id})
