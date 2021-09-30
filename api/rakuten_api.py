from flask import Flask, jsonify, request

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return jsonify({'message': 'Hello world'})

@app.route('/', methods=["GET"])
def get_user():
    input_url = request.args.getlist("input")
    # 処理
    input_food_list = input_url[0].split(',')
    return jsonify(input_food_list[0])


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8880, debug=True)