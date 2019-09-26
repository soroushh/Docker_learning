import redis
from flask import Flask
from flask import jsonify


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def set_key_value(key, value):
    cache.setex(key, 5, value)


def get_value(key):
    return cache.get(key)


@app.route('/<name>/<family>')
def hello(name, family):
    set_key_value(name, family)
    return jsonify(
        {
            "message": "It was successfully loaded to redis instance"
        }
    )

@app.route('/<name>')
def say_family(name):
    if get_value(name):
        return get_value(name)
    else:
        return jsonify({
            "message": "The family does not exist."
        })


