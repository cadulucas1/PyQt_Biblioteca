from model.livros import Livros
from model.usuario import Usuario
from controller.biblioteca import biblioteca
from controller.controller_livro import ControllerLivro
import mysql.connector

from model.livros import Livros

# Configuração do banco de dados
db_config = {
    "host": "localhost",
    "user": "seu_usuario",
    "password": "sua_senha",
    "database": "biblioteca"
}

# Inicializar a classe
livros = Livros(db_config)

# Criar tabela
livros.criar_tabela()

# Cadastrar livro
try:
    livros.cadastrar_livro("1984", "George Orwell", "1234567890123", "Distopia")
    print("Livro cadastrado com sucesso!")
except ValueError as e:
    print(f"Erro: {e}")

# Consultar livros
print("Lista de Livros:")
for livro in livros.consultar_livros():
    print(livro)

# Atualizar livro
try:
    livros.atualizar_livro(1, titulo="1984 - Edição Revisada")
    print("Livro atualizado com sucesso!")
except ValueError as e:
    print(f"Erro: {e}")

# Excluir livro
try:
    livros.excluir_livro(1)
    print("Livro excluído com sucesso!")
except ValueError as e:
    print(f"Erro: {e}")

# Fechar conexão
livros.fechar_conexao()

