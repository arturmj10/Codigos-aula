#ler arquivos - pegar um arquivo txt e dar um print nele
arquivo = 'ListaAlgoritmos.txt'
lista = []

with open(arquivo, 'r', encoding="utf-8") as file:
    n_linhas = sum(1 for line in file)
    print(n_linhas)

with open(arquivo, 'r', encoding="utf-8") as file:    
    for i in range(n_linhas):
        lista.append(file.readline())
    
lista.sort()

for i, post in enumerate(lista):
    print(f'{i+1}- {post}')

"""for indice, linha in enumerate(data):
    print(indice +1, linha)"""
    
