# __init__.py 内のappをインポート
from flask_blog import app

# URLにアクセスがあったときの処理
@app.route('/')
def show_entries():
    return "Hello World!"