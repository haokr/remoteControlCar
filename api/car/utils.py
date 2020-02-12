from socket import socket, AF_INET, SOCK_STREAM
from db import redis_cli
import re


def judge_legal_ip(one_str):
    ''''' 正则匹配方法 
    判断一个字符串是否是合法IP地址 
    '''
    compile_ip = re.compile(
        '^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?):\d{2,4}$')
    if compile_ip.match(one_str):
        return True
    else:
        return False
        
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
