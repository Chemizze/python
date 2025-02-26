def leiaInt(msg):
    while True:
        try:
            n= int(input(msg))
        except:
            print(f'\033[31mERRO por favor, digite um numero inteiro valido\033[m')
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n= float(input(msg))
        except:
            print(f'\033[31mERRO por favor, digite um numero real valido\033[m')
            continue
        else:
            return n  


n=leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')