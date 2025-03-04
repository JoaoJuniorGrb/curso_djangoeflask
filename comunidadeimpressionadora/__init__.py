from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)


app.config['SECRET_KEY']= '7fbed0a5db7ea5f367eed5f53d34db47'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

'''# 🚀 Importa os modelos ANTES de criar as tabelas
from comunidadeimpressionadora.models import Usuario, Post

with app.app_context():
    database.create_all()'''

from comunidadeimpressionadora import routes

