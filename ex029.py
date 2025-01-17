cont=0
media=soma= maior=menor=0
resp='S'
while resp in 'Ss':
    n=int(input('Digite um numero: '))
    cont+=1
    soma+=n
    resp=str(input('Quer continuar? [S/N] '))
    if cont==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n     
media=soma/cont
print('Voce digitou {} numeros e a media foi {}'.format(cont, media))
print('O numero maior {} e o menor numero foi {}'.format(maior, menor))
