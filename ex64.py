from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteiando 5 valores da lista. ', end='')
    for c in range(0, 4):
        n=randint(1, 10)
        lista.append(n)
        print(f' {n}', end ='', flush=True)
        sleep(0.5)
        
def somaPar(lista):
    soma=0
    for valor in lista:
        if valor %2==0:
            soma +=valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


num=list()
sorteia(num)
print(num)
somaPar(num)