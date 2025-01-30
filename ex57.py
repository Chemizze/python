jogador={}
jogador['nome']=str(input('Nome do jogador: '))
jogos=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['golos']=[]
jogador['total']=0

for c in range(0, jogos):
    gols=int(input(f'    Quantos gols na partida {c}? '))
    jogador['golos'].append(gols)
    jogador['total']+=gols
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas')
for i, a in enumerate(jogador['golos']):
    print(f'    => Na partida {i}, fez {a} golos')
print(f'Foi total de {jogador["total"]} golos.')
