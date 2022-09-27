from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/russel/index')
def api_hello_world():
    message = "hello world"
    return jsonify({'message': message})