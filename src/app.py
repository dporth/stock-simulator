import sys
[sys.path.append(i) for i in ['.', '..','../']]
import os
from flask import Flask
from api.users.users import users_bp
from api.accounts.accounts import accounts_bp
from api.stocks.stocks import stocks_bp
from src.db.db_helper import db_session, init_db

from flasgger import Swagger
import config

app = Flask(__name__)
app.register_blueprint(users_bp, url_prefix='/api/')
app.register_blueprint(accounts_bp, url_prefix='/api/')
app.register_blueprint(stocks_bp, url_prefix='/api/')

conf_path = os.path.abspath(__file__)
conf_path = os.path.dirname(conf_path)
conf_path = os.path.join(conf_path, 'swagger.yml')
swag = Swagger(app, template_file=conf_path)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
