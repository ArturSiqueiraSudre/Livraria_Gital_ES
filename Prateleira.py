class Prateleira():
    def __init__(self):
        self.livros = []

    def __AddLivro__(self, livro):
        self.livros.append(livro)

    def __RemoveLivro__(self, livro):
        self.livros.remove(livro)
    
    def __GetLivros__(self, Titulo, Autor):
        try:
            for livro in self.livros:
                if livro.titulo == Titulo and livro.autor == Autor:
                    print(livro.titulo)
                    return livro
            print("Livro não encontrado")
            return None
        except Exception as e:
            print("Erro encontrado ao consultar livro: ", e)

    def get_livros_por_autor(self, autor):
        for livro in self.livros: 
            if livro.autor == autor:
                return livro
        return None

    

        