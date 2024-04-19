#ler arquivos - pegar um arquivo txt e dar um print nele
arquivo = 'ListaAlgoritmos.txt'
lista = []

with open(arquivo, 'r', encoding="utf-8") as file:
    data = file.read()
    n_linhas = sum(1 for line in file)
    print(sum(1 for line in file))

"""for indice, linha in enumerate(data):
    print(indice +1, linha)"""
    
