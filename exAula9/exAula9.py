def numEntre0e10(numero):
    if(numero <=10 and numero >= 0):
        print(f"seu número é {numero} e está entre 0 e 10")
    else:
        print(f"seu é {numero} e não está entre 0 e 10")   

numEntre0e10(float(input("Digite um número: ")))

#--------------------------------------------------------------------

def menorValor(numero1, numero2, numero3):
    if(numero1 <= numero2 and numero1 <= numero3):
        return numero1
    if(numero2 <= numero1 and numero2 <= numero3):
        return numero2
    return numero3

def maiorValor(numero1, numero2, numero3):
    if(numero1 >= numero2 and numero1 >= numero3):
        return numero1
    if(numero2 >= numero1 and numero2 >= numero3):
        return numero2
    return numero3

numero1 = float(input("digite um número: "))
numero2 = float(input("digite outro número: "))
numero3 = float(input("digite outro número: "))

print(f"O maior número é {maiorValor(numero1, numero2, numero3)} e o menor é {menorValor(numero1, numero2, numero3)}")

#----------------------------------------------------------------------------------------------------------------------

def fatorialRecursivo(n):
    if n > 0:
        return n * fatorialRecursivo(n-1)
    return 1

numero = int(input("digite um número maior do que 0: "))
if numero < 0:
    print("Erro - Número negativo")
else:
    print(f"o fatorial desse número é {fatorialRecursivo(numero)}")
    
#----------------------------------------------------------------------------------------------------------------------

def calcular(calculo, n1, n2):
    if(calculo == "+"):
        return n1 + n2
    if(calculo == "-"):
        return n1 - n2
    if(calculo == "*"):
        return n1 * n2
    if(calculo == "/"):
        return n1 / n2
    return "informe um operador válido"

numero1 = int(input("digite um número inteiro: "))
numero2 = int(input("digite outro número inteiro: "))
operacao = input("Digite '+' para soma, '-' para subtração, '*' para multiplicação e '/' para divisão: ")
print(f"o resultado de {numero1} {operacao} {numero2} é {calcular(operacao, numero1, numero2)}")

