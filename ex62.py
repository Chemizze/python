from time import sleep
def contador (i, f, p):
    print(f'Contador de {i} ate {f} de {p} em {p}')
    if p <=0:
        p*=-1
    if p==0:
        p=1
    if i < f:
        for c in range(i, f+1, p):
            print(f'{c} ', end='', flush=True)
        sleep(0.5)
        print('Fim!')
    else:
        for c in range (i, f-1, -p):
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
        print('FIM!')
                     


print('-='*30)
contador(1, 10, 1)
print('-='*30)
contador(10, 0, 2)
print('-='*30)
print('Agora cria a tua propria contagem')
inicio=int(input('Inicio: '))
fim=int(input('Fim: '))
contagem=int(input('Contagem: '))
contador(inicio, fim, contagem)