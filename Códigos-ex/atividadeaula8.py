#ex 1
contadorex1 = 1
while(contadorex1 <= 44):
    print("O Cão Arrependido")
    contadorex1 += 1

#ex 2
for i in range(1,11):
    print(f'9 * {i} = {9*i}')
    
#ex 3
listaex3 = []
contadorex3 = 1
while (contadorex3 <= 10):
    listaex3.append(int(input("insira o valor: ")))
    contadorex3 += 1

listaex3.sort()
print(f'O maior valor é {listaex3[contadorex3-2]} e o menor é {listaex3[0]}')

#ex 4
listaex4 = [2,12,20,0,1,3,40,7,5,10]
listaex4.sort()
print(listaex4)