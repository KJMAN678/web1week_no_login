from flask import request, redirect, redirect, url_for, render_template, flash, session

# __init__.py 内のappをインポート
from flask_blog import app

# URLにアクセスがあったときの処理
@app.route('/')
# ログインしていないときはログインフォームへリダイレクトし、ログインしている時はホームへ移動する
def show_entries():
    # ログインしていないときの処理
    if not session.get('logged_in'):
        return redirect('/login')
    # templatesフォルダ以下にあるentries/index.html を返してレンダリングする
    return render_template('entries/index.html')

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
            # 正しい時は "/" にリダイレクト
            return redirect('/')
    # 正しくないときはログインフォームを再表示
    return render_template('login.html')

# ログアウトの処理 ホーム画面"/"に戻る
@app.route('/logout')
def logout():
    # ログアウトした場合はsession情報を削除する
    session.pop('logged_in', None)
    # ログアウトした旨のflash追加
    flash('ログアウトしました')
    return redirect('/')