#função chama a si mesmo
def somatorio(numero):
    if (numero <= 0):
        return 0
    return numero + somatorio(numero - 1)

numero = int(input("digite um número: "))
print(somatorio(numero))