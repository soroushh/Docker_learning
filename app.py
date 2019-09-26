import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def set_key_value(key, value):
    cache.set(key, value)


def get_value(key):
    cache.get(key)




@app.route('/<first>/<second>/<third>')
def hello(first, second, third):
    set_key_value(first, second)
    return cache.get(third)

