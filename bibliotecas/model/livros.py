class Livros:
    def __init__(self,titulo,autor, genero, cod_livro ):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status= "disponivel"
        self.cod_livro = cod_livro
        self.usuario = None

    def create(self):
        return f'insert into livro(título, autor, genero, status, código) values("{self.titulo}","{self.autor},"'        