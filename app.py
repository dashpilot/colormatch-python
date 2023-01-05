import os
from flask import Flask
# from color_transfer import color_transfer
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/test')
def testing():
    exec(open('transfer.py').read())
