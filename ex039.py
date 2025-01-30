n=int(input(' Digite um numero: '))
n1=int(input('Digite outro numero: '))
n2=int(input('Digite mais um numero: '))
n3=int(input('Digite o ultimo numero: '))
t=(n, n1, n2, n3 )
print(f'Voce digitou os numeros {t}')
print(f'O valor 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O valor 3 apareceu na {t.index(3)+1}ª posiçao')
else:
    print('O numero 3 nao foi digitado')
for c in t:
    if c % 2==0:
        print(f'O numero par presente é {c}')