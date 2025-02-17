def leiaInt(msg):
    ok=False
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            ok=True
        else:
            print(f'\033[31m ERRO! Digite um numero inteiro valida \033[m')
        if ok:
            break
    return valor

n=leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')