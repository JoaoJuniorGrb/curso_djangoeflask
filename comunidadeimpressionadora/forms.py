from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from comunidadeimpressionadora.models import Usuario

class FormCriarConta(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired(),Length(6,20)])
    confirmacao =PasswordField('Confirmação', validators=[DataRequired(),EqualTo('senha')])
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self,email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("Email já cadastrado, por favor fazer login ou cadastrar com novo e-mail")

class FormLogin(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    senha = PasswordField('Senha', validators=[DataRequired(),Length(6,20)])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_login = SubmitField('Login')

class FormEditarPerfil(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    botao_submit_editarperfil = SubmitField('Salvar')

