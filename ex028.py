cont=0
soma=0
n=int(input('Digite um numero [999 para parar]: '))
n=0
while n !=999:
    cont+=1
    soma+=n
    n=int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {}'.format(cont, soma))