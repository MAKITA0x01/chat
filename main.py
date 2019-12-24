from flask import Flask, request, abort ,render_template , \
                  session ,redirect , url_for

import os

# staticパスを設定。chat/static/css/〇〇〇.css とリンクしたい場合
# <link rel="stylesheet" type="text/css" href="css/〇〇〇.css">
# と、記述する。
app = Flask(__name__,static_folder='static', static_url_path='')


#---------------------------------------
# @作成者    awa-chan
# @作成日    2019/12/22
# @概要
# トップページ
#---------------------------------------
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/list")
def list():
    return render_template('list.html')

@app.route("/todo")
def index():
    return render_template('todo.html')


#---------------------------------------
# @作成者    awa-chan
# @作成日    2019/12/24
# @概要
# loginリンク押下時の処理
# GET : ログイン画面へ遷移
# POST: ログイン承認後、セッションにユーザ名を格納
#---------------------------------------

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if loginCheck(request.form["username"],request.form["password"]):
            session["username"] = request.form["username"]
            return redirect(url_for("index"))
        else:
            # TODO: 項目に応じてエラーメッセージを設定する
            errors = ["ユーザ名は1文字以上ならなんでもOK","パスワードは 1234 です。"]
            return render_template('login.html',errors = errors)

    return render_template('login.html')


## ここに承認ロジックを書く
def loginCheck(username , password):
    if password == "1234" and len(username) >= 1:
        return True
    return False

#---------------------------------------
# @作成者    awa-chan
# @作成日    2019/12/24
# @概要
# logoutリンク押下時の処理
# GET : セッションを破棄。トップページ(index)へ遷移
# POST: Not Support
#---------------------------------------
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for('index'))

#---------------------------------------
# @作成者    awa-chan
# @作成日    2019/12/24
# @概要
# myPageリンク押下時の処理
# GET : Not Support
# POST: ログインユーザ情報を表示
#---------------------------------------
@app.route("/myPage")
def myPage():
    return render_template('mypage.html')


#暗号化キー
app.secret_key = 'nanndemo_ii'

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
