from comunidadeimpressionadora import database,login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model,UserMixin):
    __tablename__ = 'Usuario'
    
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False,unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg',nullable=False)
    posts = database.relationship('Post', backref='autor', lazy=True, cascade="all, delete-orphan")
    cursos = database.Column(database.String, default='Não informado',nullable=False)

class Post(database.Model):
    __tablename__ = 'Post'
    id = database.Column(database.Integer,primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime,nullable=False,default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('Usuario.id'), nullable=True)
    
                