from datetime import datetime
pessoas={}
pessoas['nome']=str(input('Nome: '))
nasc=int(input('Ano de nascimento: '))
pessoas['idade']= datetime.now().year-nasc
pessoas['ctps']=int(input('Carteira de Trabalho (0 nao tem): '))
if pessoas['ctps']!=0:
    pessoas['contrataçao']=int(input('Ano de Contrataçao: '))
    pessoas['salario']=int(input('Salario: '))
    pessoas['aposentadorias']= pessoas['idade']+(pessoas['contrataçao']+35) - datetime.now().year
print('-='*30)
for k, v in pessoas.items():
    print(f'  ->{k} tem o valor {v} ')
