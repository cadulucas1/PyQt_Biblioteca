from model.livros import Livros
from model.usuario import Usuario
from biblioteca import biblioteca
from controller.controllerlivro import ControllerLivro
import mysql.connector

conexao = mysql.connector.connect(
   host='10.28.2.66',
   user='suporte',
   password='suporte',
   database='biblioteca'
)
