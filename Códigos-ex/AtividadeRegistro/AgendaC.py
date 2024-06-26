import numpy as np

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
      
    def __str__(self):
        return f'Nome: {self.nome}, Telefone: {self.telefone}'

class Agenda:
    def __init__(self):
        self.contatos = [None] * 50

    def cadastrarContato(self):
        print("--- Cadastrar Contato ---")
        for i in range(len(self.contatos)):
            if self.contatos[i] is None:
                nome = input("Digite o nome: ")
                telefone = input("Digite o Telefone: ")
                self.contatos[i] = Contato(nome, telefone)
                print("Contato cadastrado com Sucesso")
                input("Pressione Enter para continuar...")
                return
        print("Agenda cheia")
        input("Pressione Enter para continuar...")

    def listar(self):
        print("Lista de contatos:")
        for contato in self.contatos:
            if contato is not None:
                print(contato)
        input("Pressione Enter para continuar...")
    
    def buscar(self, nome):
        for contato in self.contatos:
            if contato is not None and contato.nome == nome:
                print("Contato encontrado:", contato)
                input("Pressione Enter para continuar...")
                return contato
        print("Contato não encontrado")
        input("Pressione Enter para continuar...")
        return None

    def remover(self, nome):
        for i in range(len(self.contatos)):
            if self.contatos[i] is not None and self.contatos[i].nome == nome:
                self.contatos[i] = None
                print("Contato removido")
                input("Pressione Enter para continuar...")
                return
        print("Contato não encontrado")
        input("Pressione Enter para continuar...")
        return None
            
agenda = Agenda()

def MenuPrincipal():
    while True:
        print("\n ======== Cadastro de Contato ========")
        print("1. Cadastrar Contato")
        print("2. Listar Contatos")
        print("3. Remover Contato")
        print("4. Buscar Contato")
        print("5. Sair")
        
        opcao = int(input("Digite o número da operação desejada: "))
        
        if opcao == 1:
            agenda.cadastrarContato()
        elif opcao == 2:
            agenda.listar()
        elif opcao == 3:
            nome = input("Digite o nome do contato a ser removido: ")
            agenda.remover(nome)
        elif opcao == 4:
            nome = input("Digite o nome do contato a ser buscado: ")
            agenda.buscar(nome)
        elif opcao == 5:
            print("Saindo do programa...")
            break
        else:
            print("Digite um valor válido")

MenuPrincipal()