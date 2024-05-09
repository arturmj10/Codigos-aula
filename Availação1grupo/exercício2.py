def numeroPerfeito(n):
    soma = 0
    for i in range(1,n):
        if (n % i) == 0:
            soma += i
    if soma == n:
        return (str(n) + " é um número perfeito")
    else:
        return (str(n) + " não é um número perfeito")

numero = int(input("digite um número inteiro e positivo: "))

if numero >= 0:
    print(numeroPerfeito(numero))
else:
    print("Digite um número inteiro e positivo")