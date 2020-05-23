from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sys

sys.path.append("/Users/kojis/anaconda3/kgs")

app = Flask(__name__)

# flask_blogフォルダいかにあるconfig.pyの内容をconfigとして指定
app.config.from_object('flask_blog.config')

# SQLAlchemy dbという変数を参照すればデータベースを扱うことが可能になる
db = SQLAlchemy(app)

from flask_blog.views import views, entries