from flask import Flask
from users.users import users_bp
import config

app = Flask(__name__)
app.register_blueprint(users_bp, url_prefix='/users')


if __name__ == "__main__":
    app.run(debug=True)