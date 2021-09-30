from flask import Flask, jsonify
from requests import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({'message': 'Hello world'})

@app.route('/', methods=["GET"])
def get_user():
    user = request.args.get("user")

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8880, debug=True)