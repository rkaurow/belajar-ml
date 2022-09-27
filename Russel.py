from flask import Flask
app = Flask(__name__)

@app.route('/russel/index')
def hello_world():
    return '<p>Hello, Dunia!<p>'