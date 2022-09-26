from flask import flask
app = flask(__name__)

@app.route("/")
def agung_lawendatu():
    return"<p>agung, lawendatu!</p>