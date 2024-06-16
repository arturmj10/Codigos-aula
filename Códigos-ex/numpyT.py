import numpy as np

lista = [1,2,3,4,5,6,7,8]

listanp = np.array([0,1,2,3,4,5,6,7])

print(listanp +1)

print(lista + lista)

print(listanp - listanp)

matriz = np.array([lista,lista,lista])
print(matriz)

print(matriz[1][2])

matriz2 = np.array([listanp, listanp, listanp])

print(matriz2)