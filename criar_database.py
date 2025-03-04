from comunidadeimpressionadora import database, app
from comunidadeimpressionadora.models import Usuario, Post  # 🚀 Importante!

# Criar o banco de dados e as tabelas
with app.app_context():
    database.create_all()
    print("✅ Banco de dados criado com sucesso!")

