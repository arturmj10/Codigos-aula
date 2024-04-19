frase = 'Eu não curto futebol'

print(frase)
print("não" in frase)
print("Não" in frase)
print("Eu" not in frase)
print(len(frase))
print(frase.lower())
print(frase.upper())
#print(dir(str))
print(frase.capitalize())
print(frase.split())

#interpolação

carro = 'Lancer'
ano = 2014
preco = 89999

#interpolação de texto
print("Carro: " + carro + ", Preço: " + str(preco) + ", Ano: " + str(ano))

#formas antigas de interpolar
print("Carro: %s, ano: %d, Preço: %f" % (carro, ano, preco))

#Versões mais novas
print("Carro: {0}, ano: {1}, Preço: {2}" .format(carro, ano, preco))

#versão atual
print(f"Carro: {carro}, ano: {ano}, Preço: {preco}")