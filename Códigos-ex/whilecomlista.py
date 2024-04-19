postagens = [
    'meu dia foi cansativo',
    'quebrei meu celular hoje',
    'meu dia foi bem legal',
    'gostei que teve sol',
    'no almoço falei bem do professor fabricio',
    'o criciúma é o maior clube do Brasil'
]
"""
contador = 0
while contador < len(postagens):
    print(postagens[contador])
    
    contador += 1
    time.sleep(3)
"""
for post in postagens:
    print(post)
    print('------')

for indice, post in enumerate(postagens): #o primeiro é indice e o segundo armazena o valor da variavel dentro do enumerate
    print(f'{indice} - {post}')
    
palavra = 'grandePalavão'

for letra in palavra:
    print(letra)
    
nomes = ('Julia', 'Artur', 'Luiz')

for nome in nomes:
    print(nome)
    
times = {'juventude', 'criciuma', 'flamengo'}

for time in times:
    print(time)