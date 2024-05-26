#Algoritmo para ler um valor de 10 posições e mostrar somente os positivos não-nulos

vetor = [int(input(f"Digite os números na posição {i+1}: ")) for i in range(10)]

for num in vetor:
    if num > 0:
        print(num)
        

# Escreva um algoritmo que leia um vetor de 15 elementos inteiros.
# Encontre e imprima na tela o menor elemento,
# assim como sua posição no vetor.

vetor = [int(input(f"Digite os números na posição {i+1}: ")) for i in range(15)]

print ("menor número", min(vetor))
print ("Index do número", (vetor.index(min(vetor))))

#Escreva um algoritmo que leia um vetor inteiro de 20
#posições (vetor 1). Verifique os valores do vetor 1 e
#modifique um segundo vetor (vetor 2), atribuindo o valor “1”
#ao vetor 2 quando houver um valor nulo no primeiro vetor.
#Ao fim, imprima os dois vetores.

vetor = [int(input(f"Digite os números na posição {i+1}: ")) for i in range(20)]
vetor1 = []
for num in vetor:
    if num == 0:
        vetor1.append(1)
    else:
        vetor1.append(num)
        
print(vetor)
print(vetor1)