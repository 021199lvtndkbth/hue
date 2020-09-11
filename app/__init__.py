from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key="\xfe\xedj\xaf\xa8\xb7\x0f\xcd\x08Y\xb9q\x15\xbf\x0e("
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:hue123@localhost/hue?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

admin = Admin(app=app, name="Quản lý bán hàng", template_mode="bootstrap3")

login = LoginManager(app=app)
