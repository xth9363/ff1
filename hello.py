from flask import Flask, escape, url_for, request
from tools.redis_tool import get_redis_conn
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(dir(request))
    print(request.url)
    redis_conn = get_redis_conn()
    redis_conn.set('now', str(datetime.now()))
    return redis_conn.get('now')


@app.route('/login')
def login():
    return 'login'


@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))


def config_redis(conf):
    redis_conf = conf.base
    _redis_pool_db0 = redis.ConnectionPool(
        host=redis_conf["host"], port=int(redis_conf["port"]), db=0, password=redis_conf["password"]
    )