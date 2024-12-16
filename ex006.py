from datetime import date
atual= date.today().year
nasc=int(input('Ano de nascimento: '))
idade=atual-nasc
print('O atleta tem {} anos'.format(idade))
if idade <10:
    print('Classifição: MIRIM')
elif idade <15:
     print('Classifição: INFANTIL')
elif idade <20:
     print('Classifição: JUNIOR')
elif idade <26:
     print('Classifição: SéNiOR')
else:
     print('Classifição: MASTER')