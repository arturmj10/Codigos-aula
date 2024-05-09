#Primeiro exercício

soma = 0
num = int(input("Digite um número inteiro e positivo: "))

for i in range(1, num):
    if num % i == 0:
        soma += i
if soma == num:
    print(num, "é um número perfeito")
else:
    print(num, "não é um número perfeito")