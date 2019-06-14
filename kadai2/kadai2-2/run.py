from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/<string:args>')
def args_page(args):
    return f'Hello {args}!'
