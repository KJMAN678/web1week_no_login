from flask import request, redirect, redirect, url_for, render_template, flash, session

# __init__.py 内のappをインポート
from flask_blog import app

# URLにアクセスがあったときの処理
@app.route('/')
def show_entries():
    # templatesフォルダ以下にあるentries/index.html を返してレンダリングする
    return render_template('entries/index.html')