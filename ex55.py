from random import randint
from time import sleep
from operator import itemgetter
jogo={'jogador1': randint(1,6), 
      'jogador2': randint(1, 6),
      'jogador3': randint(1, 6),
      'jogador4': randint(1,6)}
ranking=[]
print('Valores sorteados')
for k, v in jogo.items():
    print(f' {k} jogou {v} no dado')
    sleep(1)
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, a in enumerate(ranking):
    print(f'{i+1}º lugar: {a[0]} com {a[1]}.')
    sleep(1)