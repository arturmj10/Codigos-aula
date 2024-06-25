class Pessoa():
    def __init__(self, nome, cpf, altura, peso, idade):
        self.nome = nome
        self.cpf = cpf
        self.altura = altura
        self.peso = peso
        self.idade = idade
    
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
    pass

def alterar():
    pass

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
            
        