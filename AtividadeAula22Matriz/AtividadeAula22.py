import numpy as np

# ex1
matriz1 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(matriz1)

# ex2
matriz2 = np.random.randint(0,100, (10,10))

print(matriz2)

# ex3

matriz3 = np.empty((4,3), dtype=object)

for i in range(4):
    print(f"Cadastro pessoa {i+1}")
    matriz3[i, 0] = input("Nome: ")
    matriz3[i, 1] = input("Email: ")
    matriz3[i, 2] = input("Telefone: ")

for i in range(4   ):
    print(f"nome: {matriz3[i, 0]} |  Email: {matriz3[i, 1]} |  Telefone: {matriz3[i, 2]}")
    
# ex4

matriz4 = np.zeros((4,6), dtype=int)

for i in range(4):
    for j in range(6):
        matriz4[i,j] = int(input(f"Moradores da casa {i+1} do andar {j+1}: "))
        
print(np.sum(matriz4))

# ex5

matriz5 = np.zeros((4,4),dtype=int)

for i in range(4):
    for j in range(4):
        matriz5[i,j] = int(input(f"Digite o valor da posição [{i+1}, {j+1}]: "))
        
print(matriz5 * int(input("Digite um multiplicador para a matriz: ")))

# ex6

matriz6 = np.random.randint(0, 3, (15,10))

cadeirasDesocupadas = 0
cadeirasOcupadas = 0
cadeirasMeia = 0

for i in range(15):
    for j in range(10):
        if(matriz6[i,j] == 0):
            cadeirasDesocupadas += 1
        elif(matriz6[i,j] == 1):
            cadeirasOcupadas += 1
        elif(matriz6[i,j] == 2):
            cadeirasMeia += 1

valorCinema = (cadeirasOcupadas*12) + (cadeirasMeia*6)

print(matriz6)
print(f"\nQuantidade de acentos vazio: {cadeirasDesocupadas}")
print(f"\nQuantidade de acentos ocupados: {cadeirasOcupadas}")
print(f"\nQuantidade de acentos Meia-Entrada: {cadeirasMeia}")
print(f"\nO valor acumulado foi: {valorCinema}")
