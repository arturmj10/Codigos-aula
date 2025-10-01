class Pessoa():
    def __init__(self, nome, cpf, altura, peso, idade):
        self.nome = nome
        self.cpf = cpf
        self.altura = altura
        self.peso = peso
        self.idade = idade
    
    def __str__(self) -> str:
        return self.nome
    
    def apresentacao(self):
        return f'Prazer, meu nome é {self.nome}'
    
    def mudancaDeNome(self, nome):
        self.nome = nome
    
listaPessoa = []
def cadastrar():
    print("---Cadastrar Pessoas---")
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    altura = float(input("Digite a altura (em metros): "))
    peso = float(input("Digite o peso (em kg): "))
    idade = int(input("Digite a idade: "))
    pessoa= Pessoa(nome, cpf, altura, peso, idade)
    listaPessoa.append(pessoa)
    pass

def listar():
    print("Listagem Pessoas")
    for indice, pessoa, in enumerate(listaPessoa, start=0):
        print(f'{indice}. {pessoa}')
    

def alterar():
    print("Alteração de Pessoas")
    listar()
    
    try:
        aux = int(input("Digite o numero da pessoa que você deseja alterar: "))
        if 0  <= aux < len(listaPessoa):
            nomeNovo = input("Digite o novo nome: ")
            idadeNova = int(input("Digite a nova idade: "))
            listaPessoa[aux].nome = nomeNovo
            listaPessoa[aux].idade = idadeNova
    except ValueError:
        print("Entrada invalida")

def remover():
    pass

def MenuPrincipal():
    while True:
        print(" ======== SISTEMA DE CASDASTRO DE PESSOAS ========")
        print("1. Casatrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Alterar Pessoa")
        print("4. Remover Pessoa")
        print("5. Sair")
        
        opcao = int(input("Digite o número da operação desejada: "))
        
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            alterar()
        elif opcao == 4:
            remover()
        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Digite um valor válido")
            
MenuPrincipal()