lista=[]
cont=0
while True:
    lista.append(int(input('Digia um valor: ')))
    cont+=1
    r=' '
    while r not in 'NSsn':
        r=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('Valor 5 nao encontrado')
print('-='*30)
print(f'Voce digitou {cont} elementos')
lista,sorted(reverse=True)
print(f'Os valores em ordem decrescente so {lista}')        