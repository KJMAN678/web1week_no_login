from flask_script import Command
from flask_blog import db

# (Command)とすることでスクリプト実行のクラスとして定義される
class InitDB(Command):
    # クラス説明のためのコメント
    "create database"

    def run(self):
        db.create_all()