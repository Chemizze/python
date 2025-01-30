lista=[]
impar=[]
par=[]
while True:
    n=int(input('Digite um numero: '))
    r=' '
    if n%2==0:
        lista.append(n)
        par.append(n)
    else:
        lista.append(n)
        impar.append(n)
    while r not in 'NnSs':
        r=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')