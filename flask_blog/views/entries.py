from flask import request, redirect, redirect, url_for, render_template, flash, session

# __init__.py 内のappをインポート
from flask_blog import app
from flask_blog import db
from flask_blog.models.entries import Entry

# URLにアクセスがあったときの処理
@app.route('/')
# ログインしていないときはログインフォームへリダイレクトし、ログインしている時はホームへ移動する
def show_entries():
    # ログインしていないときの処理
    if not session.get('logged_in'):
        # url_for 関数名 で /login にリダイレクト
        return redirect(url_for('login'))

    # データベースから全ての記事を取得して、新しい順に並べ替え
    entries = Entry.query.order_by(Entry.id.desc()).all()
    # templatesフォルダ以下にあるentries/index.html を返してレンダリングする
    # index.htmlでデータベースから取得した記事が、entriesという名前で参照できるようになる。
    return render_template('entries/index.html', entries=entries)

# 予約投稿 データ送信はPOSTメソッド
@app.route('/entries', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    # ログインしていればモデルインスタンスを作成
    entry = Entry(
        title=request.form['title'],
        text=request.form['text']
    )

    # 新しい記事をデータベースへの保存
    # db.session.add(モデルインスタンス名) 新しい内容を追加
    db.session.add(entry)
    # db.session.commit() 実際にデータベースに書き込み
    db.session.commit()
    flash('新しく記事が作成されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/new', methods=['GET'])
def new_entry():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('entries/new.html')

# url_for で渡された変数idを指定する
# int:idとすることで、idに整数以外の値が入るとエラーになる
@app.route('/entries/<int:id>', methods=['GET'])
def show_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    # 渡されたidの記事をデータベースから取得することができる
    entry = Entry.query.get(id)
    return render_template('entries/show.html', entry=entry)

# 編集
@app.route('/entries/<int:id>/edit', methods=['GET'])
def edit_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    return render_template('entries/edit.html', entry=entry)

# 上書
@app.route('/entries/<int:id>/update', methods=['POST'])
def update_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    entry.title = request.form['title']
    entry.text = request.form['text']
    db.session.merge(entry)
    db.session.commit()
    flash('記事が更新されました')
    return redirect(url_for('show_entries'))

@app.route('/entries/<int:id>/delete', methods=['POST'])
def delete_entry(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    entry = Entry.query.get(id)
    db.session.delete(entry)
    db.session.commit()
    flash('投稿が削除されました！')
    return redirect(url_for('show_entries'))