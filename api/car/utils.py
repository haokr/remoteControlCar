from socket import socket, AF_INET, SOCK_STREAM
from db import redis_cli

def send(host, port, msg):
    '''向小车发送信息
    '''
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((host, port))
    s.send(msg.encode())
    s.close()


def return_result(token, msg):
    '''返回值
    '''
    token_dict = redis_cli.hgetall('token:'+token)
    host = token_dict.get('car_ip')
    port = token_dict.get('car_port')

    if not host or not port:
        return {"msg": "fail"}, 400
    send(host, port, msg)
    return {'msg': 'success'}, 200
