#ler arquivos - pegar um arquivo txt e dar um print nele
try:
    with open('C:/Users/artur/OneDrive/Área de Trabalho/arquivos/1 fase/Algoritmos e Programacao/Codigos-aula/Desafio/ListaDesafio.txt', 'r', encoding='utf-8') as arquivo:
        linhas = [linha.strip() for linha in arquivo.readlines()]
            
        linhas.sort()

        for i, linha in enumerate(linhas):
            print(f"{i+1}. {linha}")
except FileNotFoundError:
    print(f"O arquivo não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    
#Lembrando que eu usei uma lista qualquer só pra fazer a mesma coisa