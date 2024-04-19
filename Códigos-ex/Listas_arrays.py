"""
Listas - arrays ou vetores
Mutável e dinâmica, Heterogenea e indexada
"""

lista = ['Primeira Guerra Mundial', 'Segunda Guerra Mundial', 'Queda do muro de Berlin','peste negra', 'Covid-19']

print(type(lista))
#print(dir(lista))
print(lista[0])
print(lista[2])
print(lista[-1]) #ultimo item da lista
print(lista[:2]) #acessa os 2 primeiros
print(lista[1:4]) #acessa do um até o 4
print(lista[::2]) #imprime pulando de 2 em 2

lista[0] = 'alterado'
print(lista)

lista.append('Império Romano')
print(lista)

lista.remove('Queda do muro de Berlin')
print(lista)

del lista[3]
print(lista)

print(len(lista))
print(lista.count('alterado'))
print(lista.index('alterado'))

lista.reverse() #inverte a lista
lista.sort() #ordena uma lista
print(lista)
