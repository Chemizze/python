from random import randint
print('           JOGA NA MEGA SENA        ')
print('-='*30)
n=int(input('Quantos jogos voce quer que eu sorteie? '))
jogo=[]
print(f'-=-=-=-=-= SORTEANDO {n} JOGO -=-=-=--=')
for i in range(1, n+1):
    jogo.clear()
    for c in range (0, 6):
        sort=randint(1, 60)
        if sort not in jogo:
            jogo.append(sort)
        
    print(f'Jogo {i}: {sorted(jogo)}')
