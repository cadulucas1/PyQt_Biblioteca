import mysql.connector

class Livros:
    def __init__(self,titulo,autor, genero, cod_livro ):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status= "disponivel"
        self.cod_livro = cod_livro
        self.usuario = None

    def cadastrar_livro(self, titulo, autor, isbn, genero=None):
        """
        Cadastra um novo livro no banco de dados
        Título(obrigatório)
        Autor(obrigatório)
        ISBN(obrigatorio e unico)
        Caso o ISBN já esteja cadastrado dá erro.
        """
        try:
            self.cursor.execute("""
                INSERT INTO livros (titulo, autor, isbn, genero)
                VALUES (%s, %s, %s, %s)
            """, (titulo, autor, isbn, genero))
            self.conn.commit()
        except mysql.connector.IntegrityError:
            raise ValueError("O ISBN já está cadastrado.")

    def consultar_livros(self, termo=None):
        """
        Consulta livros no banco de dados
        Termo de busca (título, autor, ISBN ou gênero) 
        Se None, retorna todos os livros
        Lista de livros encontrados
        """
        if termo:
            self.cursor.execute("""
                SELECT * FROM livros
                WHERE titulo LIKE %s OR autor LIKE %s OR isbn LIKE %s OR genero LIKE %s
            """, (f"%{termo}%", f"%{termo}%", f"%{termo}%", f"%{termo}%"))
        else:
            self.cursor.execute("SELECT * FROM livros")
        return self.cursor.fetchall()

    def atualizar_livro(self, livro_id, titulo=None, autor=None, genero=None):
        """
        Atualiza informações de um livro no banco de dados.
        ID do livro a ser atualizado
        Novo título do livro (opcional)
        Novo autor do livro (opcional)
        Novo gênero do livro (opcional)
        Caso o livro não exista da erro
        """
        self.cursor.execute("SELECT * FROM livros WHERE id = %s", (livro_id,))
        if not self.cursor.fetchone():
            raise ValueError("Livro não encontrado.")

        updates = []
        valores = []

        if titulo:
            updates.append("titulo = %s")
            valores.append(titulo)
        if autor:
            updates.append("autor = %s")
            valores.append(autor)
        if genero:
            updates.append("genero = %s")
            valores.append(genero)

        if updates:
            query = f"UPDATE livros SET {', '.join(updates)} WHERE id = %s"
            valores.append(livro_id)
            self.cursor.execute(query, tuple(valores))
            self.conn.commit()

    def excluir_livro(self, livro_id):
        """
        Exclui um livro do banco de dados.
        ID do livro a ser excluído.
        Caso o livro esteja emprestado ou não exista.
        """
        # Verificar se o livro está emprestado
        self.cursor.execute("""
            SELECT COUNT(*) FROM emprestimos WHERE id_livro = %s AND data_devolucao IS NULL
        """, (livro_id,))
        emprestado = self.cursor.fetchone()["COUNT(*)"]

        if emprestado > 0:
            raise ValueError("O livro está emprestado e não pode ser excluído.")

        # Verificar existência do livro
        self.cursor.execute("SELECT * FROM livros WHERE id = %s", (livro_id,))
        if not self.cursor.fetchone():
            raise ValueError("Livro não encontrado.")

        self.cursor.execute("DELETE FROM livros WHERE id = %s", (livro_id,))
        self.conn.commit()

    def fechar_conexao(self):
        """
        Fecha a conexão com o banco de dados.
        """
        self.cursor.close()
        self.conn.close()       