# Import Library 
from flask import Flask
from flask_httpauth import HTTPBasicAuth

#Flask、HTTPBasicAuthクラスのインスタンスを作成
app = Flask(__name__)
auth = HTTPBasicAuth()

# 認証可能なID/Password
id_list = {
    "Tanaka": "1111",
    "Suzuki": "1234"
}

# 認証用の関数
@auth.get_password
def get_pw(id):
    if id in id_list:
        return id_list.get(id)
    return None

@app.route('/')
# 認証関数の呼び出し
@auth.login_required
# 認証許可後の処理
def index(): 
    return "Hello, %s!" % auth.username()

if __name__ == '__main__':
    app.run()