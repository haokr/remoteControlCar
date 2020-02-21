from socket import socket, AF_INET, SOCK_STREAM
from db import redis_cli
import re
from socket_io import socketio
import json

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
    data = {
        'host': "139.196.94.212",
        "port": "9030",
        "msg": msg
    }
    s.send(json.dumps(data).encode())
    s.close()


