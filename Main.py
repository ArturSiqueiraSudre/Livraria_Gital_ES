import pytest
import Livros
import Prateleira

def test_adiciona_e_busca_livro():
    livro = Livros.Livros("1984", "George Orwell",1990, 10.99)
    prateleira = Prateleira.Prateleira()
    prateleira.__AddLivro__(livro)

    resultado = prateleira.__GetLivros__("1984", "George Orwell")
    assert resultado.__GetAno__()
    assert resultado.__GetPreço__()

def test_lista_livros_filtrada():
    prateleira = Prateleira.Prateleira()
    livro1 = Livros.Livros("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 50.00)
    livro2 = Livros.Livros("O Hobbit", "J.R.R. Tolkien", 1937, 30.00)
    livro3 = Livros.Livros("Dom Casmurro", "Machado de Assis", 1899, 20.00)

    prateleira.__AddLivro__(livro1)
    prateleira.__AddLivro__(livro2)
    prateleira.__AddLivro__(livro3)

    # Filtra livros do autor J.R.R. Tolkien
    livros_fAutor = prateleira.get_livros_por_autor("J.R.R. Tolkien")

    # Filtra livros do 1954
    livros_fAnos = prateleira.get_livros_por_ano(1954)
    
    livros_fPreco = prateleira.get_livros_RangePreco(30, 50)
    
    assert len(livros_fAutor) == 2
    assert all(l.autor == "J.R.R. Tolkien" for l in livros_fAutor)

    assert len(livros_fAnos) == 1
    assert all(l.ano == 1954 for l in livros_fAnos)

    assert len(livros_fPreco) == 2
    assert all(l.preco >= 30 and l.preco <= 50 for l in livros_fPreco)

if __name__ == "__main__":  
    # Executa os testes utilizando o pytest
    pytest.main([__file__])
