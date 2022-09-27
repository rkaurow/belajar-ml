from flask import Flask
from flask import jsonify

app = Flask(__name__)
@app.route('/nofrets/hello-world')
def api_hello_world():
    first_name = "Nofrets"
    last_name = "Poai"
    age = 17
    return jsonify({
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        })

@app.route('/nofrets/user')
def api_user():
    id = "123456789"
    first_name = "Poai"
    last_name = "Poai"
    age = 17
    email = 'nofrets.poai@gmail.com'
    return jsonify({
        'id': id,
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'email': email,
        })