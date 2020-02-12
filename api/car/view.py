from flask import g, request, abort
from . import car
from . import utils
from db import redis_cli

@car.route('/run', methods=['POST'])
def run():
    msg = None
    isbackward = request.form.get('backward')
    if isbackward:
        msg = 'forward'
    else:
        msg = 'backward'

    token = request.args.get('token')
    return utils.return_result(token, msg)

@car.route("/turn", methods=['POST'])
def turn():
    msg = None
    isleft = request.form.get('left')
    if isleft:
        msg = 'left'
    else:
        msg = 'right' 

    token = request.args.get('token')
    return utils.return_result(token, msg)

@car.route("/gear", methods=['POST'])
def gear():
    msg = None
    isfast = request.form.get("fast")
    if isfast:
        msg = 'fast'
    else:
        msg = 'slow'
    
    token = request.args.get('token')
    return utils.return_result(token, msg)

@car.route('/lock', methods=["POST"])
def lock():
    msg = None
    isopen = request.form.get('open')
    if isopen:
        msg = 'lock'
    else:
        msg = 'unlock'
    
    token = request.args.get('token')
    return utils.return_result(token, msg)
