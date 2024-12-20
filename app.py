from flask import Flask, jsonify, request
from flask_cors import CORS
import os #追加

app = Flask(__name__)
# CORS設定を更新
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "https://tech0-gen-8-step3-testapp-node-oka-ggh6cxc6avama5bk.canadacentral-01.azurewebsites.net",
            "http://localhost:3000" # ローカル開発⽤1
        ]
    }
})

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'message': 'Flask start!'})

@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message='Hello World by Flask')

@app.route('/api/multiply/<int:id>', methods=['GET'])
def multiply(id):
    print("multiply")
    # idの2倍の数を計算
    doubled_value = id * 2
    return jsonify({"doubled_value": doubled_value})

@app.route('/api/echo', methods=['POST'])
def echo():
    print("echo")
    data = request.get_json()  # JSONデータを取得
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    # 'message' プロパティが含まれていることを確認
    message = data.get('message', 'No message provided')
    return jsonify({"message": f"echo: {message}"})

if __name__ == '__main__':
    # 環境変数PORTを取得（デフォルトは8000）
    port = int(os.environ.get('PORT', 8080))
    # デバッグモードをローカル環境では有効に、本番では無効に
    app.run(host='0.0.0.0', port=port, debug=False)
