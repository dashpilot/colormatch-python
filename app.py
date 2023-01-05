from flask import Flask
# from color_transfer import color_transfer
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/test')
def test():
    file = open('transfer.py', 'r').read()
    return exec(file)
