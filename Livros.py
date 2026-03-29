class Livros():
    def __init__(self, titulo, autor, ano, preco):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.preco = preco

    
    def __GetTitulo__(self):
        return self.titulo
    
    def __GetAutor__(self):
        return self.autor
    
    def __GetAno__(self):
        return self.ano
    
    def __GetPreço__(self):
        return self.preco
    
    def __SetTitulo__(self, titulo):
        self.titulo = titulo
    
    def __SetAutor__(self, autor):
        self.autor = autor
    
    def __SetAno__(self, ano):
        self.ano = ano
    
    def __SetPreço__(self, preco):
        self.preco = preco
    
    