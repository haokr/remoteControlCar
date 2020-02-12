import time
import random
import string
import shortuuid
from db import redis_cli

DURATION = 60 * 30

class Token():
    def __init__(self, user_id, car_ip=='', car_port=''):
        self.token = self._gen_token(user_id, car_ip, car_port)
        self.user_id = user_id
        self.car_ip = car_ip
        self.car_port = car_port

    def _gen_token(self, user_id, car_ip, car_port):
        '''生成token并保存到Redis，token内容为：{"user_id":user_id, "car_ip":car_ip}
        '''
        token_id = shortuuid.uuid()
        key = 'token:'+ token_id
        pipe = redis_cli.pipe()
        pipe.hmset(key, mapping={'user_id': user_id, 'car_ip': car_ip, "car_port": car_port})
        pipe.expire(key, DURATION)
        pipe.execute()
        return token_id

    @staticmethod
    def token_auth(token):
        '''验证token，如果token不存在返回False，如果token ttl小于DURATION值的一半重新设置expire
        '''
        pipe = redis_cli.pipe()
        token_dict = pipe.hgetall('token:'+token)

        if not token_dict:
            return False
        ttl = pipe.ttl("token:"+token)
        if ttl < DURATION//2:
            pipe.expire(token, DURATION)
        pipe.execute()

        if not token_dict.get('user_id'):
            raise "Token have not user_id"
        if not token_dict.get('car_ip') or not token_dict.get("car_port"):
            raise "Token have not car_ip or car_port"
        return True



