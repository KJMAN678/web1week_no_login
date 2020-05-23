from flask import Flask

app = Flask(__name__)

# flask_blogフォルダいかにあるconfig.pyの内容をconfigとして指定
app.config.from_object('flask_blog.config')

import flask_blog.views