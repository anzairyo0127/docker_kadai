from flask import Flask

from model import redis_cli


app = Flask(__name__)


@app.route('/')
def index():
    return redis_cli.get('test')
