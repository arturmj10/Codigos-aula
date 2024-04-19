"""
#ex 1
numero_ex1 = int(input("Digite um número: "))
soma_ex1 = 0
for i in range(numero_ex1 - 1, 0, -1):
    soma_ex1 = soma_ex1 + i
print(f"A soma entre todos os números menores que o número {numero_ex1} até 0 é {soma_ex1}")
"""
#ex 2
fator = 0
idade = 0
while fator < 5:
    idade = idade + int(input(f"digite a {fator+1}ª idade: "))
    fator += 1
media = idade/fator
print(media)

#ex 3
numero_ex3 = int(input("Digite o número menor: "))
numero2_ex3 = int(input("Digite o número maior: "))
for i in range(numero_ex3 + 1, numero2_ex3):
    if i % 2 == 0:
        print(i)

#ex 4
numero_ex3 = int(input("Digite o número menor: "))
numero2_ex3 = int(input("Digite o número maior: "))
for i in range(numero_ex3 + 1, numero2_ex3):
    if i % 2 != 0:
        print(i)     

#ex 5
soma = 0
numero_ex5 = 0
while numero_ex5 >= 0:
    soma = soma + numero_ex5 
    numero_ex5 = int(input("digite um número inteiro (negativo para sair): "))
print(f"a soma dos numeros digitados é {soma}")

#ex 6
fator = 0
soma = 0
while fator < 5:
    soma = soma + int(input(f"digite o {fator+1}º número: "))
    fator += 1
if soma % 2 != 0:
    print(f"a soma desses números é impar e é: {soma}")
else:
    print(f"a soma desses números é par e é: {soma}")

#ex 7
numero_ex7 = int(input("Digite um número inteiro positivo: "))

if(numero_ex7 <=1):
    ehprimo = False
elif numero_ex7 == 2:
    ehprimo = True
else:
    for i in range(2, numero_ex7):
        ehprimo = True
        if(numero_ex7 % i == 0):
            ehprimo = False
            break
if(ehprimo):
    print(f"O número {numero_ex7} é primo")
else:
    print(f"O número {numero_ex7} não é primo")

#ex 8
numero_ex8 = int(input("digite um número inteiro: "))
i = 1
while(i <= 10):
    print(f"{numero_ex8} x {i} = {i*numero_ex8}")
    i += 1

#ex 9
numero_ex9 = int(input("digite um número inteiro: "))
print(f"O dobro de todos os números entre 0 e {numero_ex9}: ")
for i in range(0, numero_ex9):
    print(i * 2)
