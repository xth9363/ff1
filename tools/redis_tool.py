import redis

HOST = 'localhost'
PORT = '6379'
PASSWORD = ''


def get_redis_conn():
    r_db = redis.Redis(host=HOST,
                       port=PORT,
                       password=PASSWORD,
                       decode_responses=True,   # decode_responses=True，写入value中为str类型，否则为字节型
                       db='2')     # 默认不写是db0
    # r_db.set('name','zhangsan')
    return r_db

