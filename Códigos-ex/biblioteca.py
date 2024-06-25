class Livro:
    def __init__(self, nome, paginas) -> None:
        self.nome = nome
        self.paginas = paginas
        pass
    
    def __str__(self) -> str:
        return f'{self.nome} | {self.paginas}'
    
    def apresentacao(self):
        return f'prazer meu nome é {self.nome}'
    
    def mudancaNome(self, nome):
        self.nome = nome
    
livro1 = Livro("Harry Potter", 230)

print(livro1)

del livro1