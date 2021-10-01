from os import error
from flask import Flask, jsonify, request
import api.rakuten_api as API

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return jsonify({'message': 'Hello world'})

@app.route('/', methods=["GET"])
def get_user():
    input_url = request.args.getlist("input")
    # 処理
    input_food_list = input_url[0].split(',')
    Rakuten_api = API.rakuten_api() # インスタンス作成
    sorted_api_result = Rakuten_api.call_api(input_food_list=input_food_list) # 楽天APIを呼び出し，食材のマッチ数が多い順にソートされたjsonデータを取得する
    recipe_list = Rakuten_api.output_recipe(recipe_num=5, sorted_api_result=sorted_api_result) # レシピの出力
    
    # return json.dumps(recipe_list, default=str)
    return jsonify(recipe_list)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8880, debug=True)