from flask import Flask
from color_transfer import color_transfer
app = Flask(__name__)

@app.route('/')
def hello():
    return(color_transfer())
