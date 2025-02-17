def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} marcou {g} golos.')




nome=str(input('Nome do Jogador: '))
gols=str(input('Numero de gols: '))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0
if nome.strip()=='':
    ficha(g=gols)
else:
    ficha(nome, gols)   
    

