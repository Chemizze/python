from random import randint
from time import sleep
computador= randint(0, 10)
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10')
sleep(1)
print('Sera que voce consegue adivinhar qual foi? ')
sleep(1)
acertou=False
palpite=0
while not acertou:
    jogador= int(input('Qual o seu palpite: '))
    palpite+=1
    if jogador == computador:
        acertou=True
    else:
        if jogador < computador:
            print('Mais...')
        else:
            print('Menos...')
print('Acertou com {} tentativas.'.format(palpite))
