alunos = [
    {'nome': 'Diva', 'notas': [9,8,10]},
    {'nome': 'Artur', 'notas': [9,8,10]},
    {'nome': 'Arthur', 'notas': [9,8,10]},
    {'nome': 'Victor', 'notas': [9,8,10]},
]

def calcular_media(notas):
    totalNotas = 0
    for nota in notas:
        totalNotas += nota
    
    media = totalNotas/len(notas)
    return media

for aluno in alunos:
    nome = aluno['nome']
    notas = aluno['notas']
    
    print(f'Média do(a) {nome} é {calcular_media(notas)}')
    
def somar(a, b, c):
    total = a+b+c;
    print(f'total:  {total}')

somar(1,2,3)

# packing
def somar2(*numeros):
    #empacotando de uma tupla
    print(type(numeros))
    total = 0;
    for num in numeros:
        total += num
    
    print(f"o total é {total}")
    
somar2(10,20,30,40)