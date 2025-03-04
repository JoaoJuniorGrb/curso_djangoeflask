from flask import Flask,render_template, url_for,request,flash,redirect
from comunidadeimpressionadora import app,database,bcrypt
from comunidadeimpressionadora.forms import FormCriarConta,FormLogin,FormEditarPerfil
from comunidadeimpressionadora.models import Usuario,Post
from flask_login import login_user,logout_user,current_user, login_required

lista_usuarios=['João','Alon','Alessandra','martina']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash('Logout feito com sucesso', 'alert-success')
    return redirect(url_for('home'))

@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static',filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)

@app.route('/perfil/editar',methods=['GET','POST'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    foto_perfil = url_for('static',filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)


@app.route('/post/criar')
@login_required
def criar_post():
    return render_template('criar_post.html')

@app.route('/usuarios')
@login_required
def usuarios():
    return render_template('usuarios.html',lista_usuarios=lista_usuarios)

@app.route('/login',methods=['GET','POST'])
def login():
    form=FormLogin()
    form_criarconta=FormCriarConta()

    if form.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha,form.senha.data):
            login_user(usuario,remember=form.lembrar_dados.data)
            flash(f'Login feito com sucesso no email: {form.email.data}', 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Email ou Senha incorreto', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data,email=form_criarconta.email.data,senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada com sucesso no email: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html',form=form,form_criarconta=form_criarconta)
