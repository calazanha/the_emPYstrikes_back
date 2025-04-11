class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"{self.titulo} de {self.autor} com {self.paginas} páginas"

    def __len__(self):
        return self.paginas

livro = Livro("Dom Casmurro", "Machado de Assis", 240)
print(livro)
print("Páginas:", len(livro))
