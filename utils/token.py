import time
import random
import string
import shortuuid
from db import redis_cli

DURATION = 60 * 30

class Token():
    def __init__(self, user_id, car_id='', car_ip='', car_port=''):
        '''生成token并保存到Redis，token: token:token_id:user_id:car_id,内容为：{"car_ip": ip, "car_port": port}
        '''
        token_id = shortuuid.uuid()
        key = f'token:{token_id}:{user_id}:{car_id}'
        pipe = redis_cli.pipeline()
        pipe.hmset(key, mapping={'car_ip': car_ip, "car_port": car_port})
        pipe.expire(key, DURATION)
        pipe.execute()
        self._token = token_id

    def get(self):
        return self._token

    @staticmethod
    def auth(token):
        '''验证token，如果token不存在返回False，如果token ttl小于DURATION值的一半重新设置expire
        '''
        # 根据token获取key
        matched_keys = redis_cli.keys(f'token:{token}:*:*')
        if not matched_keys:
            return False
        key = matched_keys[0]
        token_dict = redis_cli.hgetall(key)

        ttl = redis_cli.ttl(key)
        if ttl < DURATION//2:
            redis_cli.expire(key, DURATION)

        return {
            'user_id': token_dict.get('user_id'),
            'car_ip': token_dict.get('car_ip'),
            'car_port': token_dict.get('car_port')
        }



