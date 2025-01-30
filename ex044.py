lista=[]
while True:
    n=int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Nao foi adicionado. Voce duplicou o numero')
    r=' '
    while r not in 'NnSs':
        r=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
print(f'Voce digitou os valores {sorted(lista)}')