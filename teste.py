'''from comunidadeimpressionadora import app,database
from comunidadeimpressionadora.models import Usuario, Post


#criação do banco de dados
with app.app_context():
    database.create_all()'''


'''
#buscando primeiro usuario
with app.app_context():
    meus_usuarios = Usuario.query.first()
    print(meus_usuarios.username)

#buscando por filtro
with app.app_context():
    meus_usuarios = Usuario.query.filter_by(id=1).first()
    print(meus_usuarios.username)
    print(meus_usuarios.email)


#criando post
with app.app_context():
    meu_post= Post(id_usuario=1, titulo='Primeiro post',corpo='olá')
    database.session.add(meu_post)
    database.session.commit()
   

#buscando post por filtro
with app.app_context():
    post = Post.query.filter_by(id=1).first()
    print(post.titulo)
    print(post.autor.email)

#deletar todo banco de dados
with app.app_context():
    database.drop_all()
    database.create_all()'''

'''from comunidadeimpressionadora import database, app
from sqlalchemy import text

with app.app_context():
    result = database.session.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    tables = result.fetchall()
    print(tables)  # Deve exibir [('usuario',), ('post',)] se tudo estiver correto
'''
'''
from comunidadeimpressionadora import database, app
from sqlalchemy import text


with app.app_context():
    result = database.session.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    print(result.fetchall())  # Deve exibir [('Usuario',), ('Post',)]
'''

from comunidadeimpressionadora import database, app
from sqlalchemy import text

with app.app_context():
    # Listar todas as tabelas no banco
    result = database.session.execute(text("SELECT name FROM sqlite_master WHERE type='table';"))
    tabelas = [t[0] for t in result.fetchall()]
    print(f"Tabelas no banco: {tabelas}\n")

    # Percorrer cada tabela e exibir os dados
    for tabela in tabelas:
        print(f"Conteúdo da tabela {tabela}:")
        result = database.session.execute(text(f"SELECT * FROM {tabela};"))
        colunas = [col[0] for col in result.cursor.description]  # Pega os nomes das colunas
        dados = result.fetchall()
        
        if dados:
            print(f"{colunas}")
            for linha in dados:
                print(linha)
        else:
            print("🔴 Nenhum dado encontrado.")
        print("\n" + "="*50 + "\n")
