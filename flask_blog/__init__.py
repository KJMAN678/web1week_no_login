from flask import Flask

import flask_blog.views

app = Flask(__name__)

# flask_blogフォルダいかにあるconfig.pyの内容をconfigとして指定
app.config.from_object('flask_blog.config')