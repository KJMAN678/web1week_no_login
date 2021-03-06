from flask import request, redirect, redirect, url_for, render_template, flash, session

# __init__.py 内のappをインポート
from flask_blog import app

# /login というURLにリクエストがあったときのルーティング処理
# method を指定するとこのURLに対するHTTPメソッドを制限できる
# 指定しないとGETメソッドのみ指定される
# login リンクをクリックするときはGETメソッド、ログインフォームのデータ送信にはPOSTメソッドが使われる
@app.route('/login', methods=['GET', 'POST'])
def login():
    # POSTメソッドでリクエストがあったとき＝ログインフォームに入力されたデータがおくられたときの処理が記載できる。
    # GETメソッド＝/loginをクリックした場合はこの処理はされない
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            # flashに変更
            flash('ユーザー名が異なります')
        elif request.form['password'] != app.config['PASSWORD']:
            # flashに変更
            flash("パスワードが異なります")
        else:
            # sessionという変数を使用 logged_inにTrueがセットされることで、ログインしていることを表す 
            session['logged_in'] = True
            # ログインした旨のflash追加
            flash('ログインしました')
            # url_for 関数名 で"/"にリダイレクト
            return redirect(url_for('show_entries'))
    # 正しくないときはログインフォームを再表示
    return render_template('login.html')

# ログアウトの処理 ホーム画面"/"に戻る
@app.route('/logout')
def logout():
    # ログアウトした場合はsession情報を削除する
    session.pop('logged_in', None)
    # ログアウトした旨のflash追加
    flash('ログアウトしました')
    # url_for 関数名 で / にリダイレクト
    return redirect(url_for('show_entries'))