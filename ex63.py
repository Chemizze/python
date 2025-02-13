from time import sleep
def maior(*num):
    cont=maior=0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.5)
        if cont ==1:
            maior== valor
        else:
            if valor > maior:
                maior=valor
        cont+=1
    print()
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
maior(2,6,7,1,3)
maior(4,7,8)
maior(1,2)
maior(6)
maior(7)