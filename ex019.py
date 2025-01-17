from datetime import date
atual = date.today().year
totmaior=0
totmenor=0
for pess in range(1, 8):
    nasc=int(input('Em que ano a pessoa nasce? '))
    idd= atual - nasc
    if idd >= 21:
        totmaior+=1
    else:
        totmenor+=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E tambem tivermos {} pessoas menores de idade'.format(totmenor))