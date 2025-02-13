time=[]
jogador={}
jogador['golos']=[]
while True:
    jogador.clear()
    jogador['nome']=str(input('Nome do jogador: '))
    jogos=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['total']=0
    for c in range(0, jogos):
        gols=int(input(f'    Quantos gols na partida {c}? '))
        jogador['golos'].append(gols)
        jogador['total']+=gols
    time.appens(jogador.copy())
    while True :
        resp=str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN ':
            break
    if resp == 'N':
        break
    
print('-='*30)
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}' ,end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print(jogador)
print('-='*30)
