alunos=[]
while True:
    nome=str(input('Nome: '))
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    alunos.append([nome, [nota1, nota2], media])
    r=' '
    while r not in 'NSsn':
        r=str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print('-='*20)
print(f'{"No." :<4}{"NOME":<10}{"MEDIA":>8}')
print('-='*20)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-='*26)
    no=int(input('Qual aluno queres ver as notas?(999 para interromper) '))
    if no ==999:
        break
    if no <= len(alunos):
        print(f'As notas do {alunos[no]} sao {alunos[no][1]}')