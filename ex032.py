from random import randint
v=0
while True:
  jogador=int(input('Diga um valor: '))
  computador=randint(0,10)
  total=jogador+computador
  tipo=str(input('Par ou impar? [P/I]: ')).strip().upper()[0] 
  print(f'Voce jogou {jogador} e o computador jogou {computador}. O total de {total}')
  if tipo =='P':
      if total %2 == 0:
          print('Voce venceu!')
          v+=1
      else:
          print('Voce perdeu!')
          break
  elif tipo =='I':
      if total %3==0:
          print('Voce venceu!')
          v+=1
      else:
          print('Voce perdeu!')
          break
      print('Vaamos jogar novamente!!')
print(f'GAME OVER!! Voce venceu {v} vezes ')
