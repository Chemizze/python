cont=media=soma=0
pessoa={}
pessoas=[pessoa]
while True:
    pessoa.clear
    pessoa['nome']=str(input('Nome: '))
    pessoa['sexo']=' '
    pessoa['idade']=int(input('Idade: '))
    while pessoa['sexo'] not in 'MFmf':
        pessoa['sexo']= str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] not in 'MmFf':
          print('ERRO! Por favor, digite apenas M ou F')
    r=' '
    soma+=pessoa['idade']
    cont+=1
    pessoas.append(pessoa.copy())
    while r not in 'SnNs':
        r=str(input('Quer continuar? [N/S] ')).strip().upper()[0]
        if r not in 'SNsn':
         print('ERRO! Responde apenas com S ou N')
    if r in 'Nn':
        break
print('-='*30)
media=soma/cont   
print(f'A) Ao todo temos 4 pessoas cadastradas') 
print(f'B) A media de idade é de {media:.2f} anos') 
print(f'C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end='')
print()
print(f'D) Lista das pessoas que estao acima da media: ')    
for p in pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
          print(f' {k}= {v}; ', end='') 
       
print('\n<<ENCERRADO>>') 
    
