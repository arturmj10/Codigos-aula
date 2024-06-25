import numpy as np

class Contato():
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
      
    
    def __str__(self) -> str:
        return f'Nome: {self.nome}, Telefone: {self.telefone}'
    

class Agenda():
    
    def __init__(self):
        self.contatos = np.zeros(50, dtype=Contato)
        
    def cadastrarContato(self):
        print("---Cadastrar Contato---")
        for i in range(len(self.contatos)):
            if self.contatos[i] is None:
                nome = input("Digite o nome: ")
                telefone = input("Digite o Telefone: ")
                contato = Contato(nome, telefone)
                self.contatos[i] = contato
                print("Contato cadastrado com Sucesso")
            return
        print("Agenda cheia")
        
    def listar(self):
        print("Lista de contatos:")
        for contato in self.contatos:
            if contato is not None:
                print(contato)
        return None
    
    def buscar(self, nome):
        for contato in self.contatos:
            if contato is not None and contato.nome == nome:
                return contato
        return None

    def remover(self, nome):
        for contato in self.contatos:
            if contato is not None and contato.nome == nome:
                self.contato = None
                print("Contato removido")
        print("Contato não encontrado")
        return None
            
agenda = Agenda()


def MenuPrincipal():
    while True:
        print(" ======== Cadastro de Contato ========")
        print("1. Casatrar Contato")
        print("2. Listar Contato")
        print("3. Remover Contato")
        print("4. Buscar Contato")
        print("5. Sair")
        
        opcao = int(input("Digite o número da operação desejada: "))
        
        if opcao == 1:
            agenda.cadastrarContato()
        elif opcao == 2:
            agenda.listar()
        elif opcao == 3:
            agenda.remover()
        elif opcao == 4:
            agenda.buscar
        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Digite um valor válido")
            
MenuPrincipal()

