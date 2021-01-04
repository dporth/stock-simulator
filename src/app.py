import sys
[sys.path.append(i) for i in ['.', '..','../']]
from flask import Flask
from api.api import api_bp
import config

app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')


if __name__ == "__main__":
    app.run(debug=True)