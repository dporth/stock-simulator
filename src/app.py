import sys
[sys.path.append(i) for i in ['.', '..','../']]
from flask import Flask
from api.users.users import users_bp
from api.accounts.accounts import accounts_bp
import config

app = Flask(__name__)
app.register_blueprint(users_bp, url_prefix='/api/')
app.register_blueprint(accounts_bp, url_prefix='/api/')


if __name__ == "__main__":
    app.run(debug=True)