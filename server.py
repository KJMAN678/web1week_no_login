from flask_blog import app
import os
import sys

sys.path.append("/Users/kojis/anaconda3/kgs")

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)