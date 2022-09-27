from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/russel/index')
def index():
    return jsonify({'message':'Hello, Dunia!'})