import pytest
import Livros
import Pratileira

def test_adiciona_e_busca_livro():
    livro = Livros.Livros("1984", "George Orwell", 1990, 10.99)
    prateleira = Prateleira()
    prateleira.add_livro(livro)

    resultado = prateleira.get_livro("1984", "George Orwell")
    assert resultado.Ano == 1990
    assert resultado.Preco == 10.99

def test_lista_livros_filtrada():
    prateleira = Prateleira()
    livro1 = Livros.Livros("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 50.00)
    livro2 = Livros.Livros("O Hobbit", "J.R.R. Tolkien", 1937, 30.00)
    livro3 = Livros.Livros("Dom Casmurro", "Machado de Assis", 1899, 20.00)

    prateleira.add_livro(livro1)
    prateleira.add_livro(livro2)
    prateleira.add_livro(livro3)

    # Filtra livros do autor J.R.R. Tolkien
    livros_filtrados = prateleira.get_livros_por_autor("J.R.R. Tolkien")
    
    assert len(livros_filtrados) == 2
    assert all(l.autor == "J.R.R. Tolkien" for l in livros_filtrados)

if __name__ == "__main__":
    # Executa os testes utilizando o pytest
    pytest.main([__file__])
