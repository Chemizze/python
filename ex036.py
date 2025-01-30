n=('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', ' sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')
cont=0
while True:
    r=int(input('Digite um numero entre 0 e 20: '))
    print(f'Voce digitou o numero {n[r]}')
    resp=' '
    while resp not in 'NSsn':
        resp=str(input('Queres continuar? [S/N] ')).strip().upper()[0]
    cont+=1
    if resp in 'Nn':
          break   
print(f'Digitaste {cont} numeros')     