from flask_blog import db
from datetime import datetime

# モデル名をEntryとする
class Entry(db.Model):
    __tablename__ = 'entries'

    # 属性名の定義 primary_keyは記事を特定するための番号でモデル内で1つとする必要あり
    id = db.Column(db.Integer, primary_key=True)
 
    # String(50)は50文字以内ということを指す
    # unique=True は重複しないことを指す
    title = db.Column(db.String(50), unique=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime)

    # モデルが作成されたときの標準の挙動を定義
    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text
        self.created_at = datetime.utcnow()

    # 記事も出るが参照されたときのコンソールでの出力形式。なくてもOK
    def __repr__(self):
        return '<Entry id:{} title:{} text:{}>'.format(self.id, self.title, self.text)