"""
#Função exige return, geralmente do tipo que foi criada a função
def soma(a, b): 
    return a+b

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(soma(numero1, numero2))

#Procedimento não tem return
def soma2(a, b): 
    print(f"o resultado é {a+b}")

numero3 = int(input("Digite o primeiro número: "))
numero4 = int(input("Digite o segundo número: "))

soma2(numero3, numero4)
"""
def soma_a_0():
    soma = 0
    numero = int(input("Escreva um número inteiro e maior que zero: "))
    if(numero <= 0):
        print("Erro! Digite um número maior que 0")
        return 0
    
    for i in range(numero, 0, -1):
        soma = soma + i
        
    print(soma)
    
soma_a_0()
