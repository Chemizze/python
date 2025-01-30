aluno={}
nome=str(input('Nome: '))
aluno['nome']=nome
media=float(input(f'Media de {nome}: '))
aluno['media']=media
print('-='*15)
print(f'  ->nome é igual a {aluno["nome"]}')
print(f'  ->media é igual a {aluno["media"]}')
if media >=7.0:
   print(f'  ->situaçao é igual a Aprovado')
else:
    print('  ->situaçao é igual a REPROVADO')
