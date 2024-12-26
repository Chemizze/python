from random import randint
from time import sleep
itens=('Pedra', 'Papel', 'Tesoura')
computador= randint(0, 2)
print('''Suas opçoes:
      [0] PEDRA
      [1] PAPEL
      [2] TESOURA''')
jogador=int(input('Qual a tua jogada?: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*12)
if computador == 0:
  if jogador==0:
        print('EMPATOU')
  elif jogador==1:
        print('O jogador venceu!')
  elif jogador==2:
        print('O computador venceu')
  else:
        print('JOGADA INVALIDA')
elif computador==1:
      if jogador==0:
            print('JOGADOR VENCEU')
      elif jogador==1:
            print('EMPATE')
      elif jogador==2:
            print('JOAGAR VENCEU')
      else:
        print('JOGADA INVALIDA')
elif computador==2:
      if jogador==0:
            print('JOGADOR VENCEU')
      elif jogador==1:
            print('COMPUTADOR VENCEU')
      elif jogador==2:
            print('EMPATOU')
      else:
        print('JOGADA INVALIDA')
