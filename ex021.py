maior=0
menor=0
somaidade=0
fem=0
nomevelho=''
for c in range(1, 5):
    print('-'*5, end=' ')
    print('{}ª Pessoa'.format(c), end =' ')
    print('-'*5)
    nome=str(input('Nome: ')).strip()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip()
    somaidade+=idade
    if c== 1 and sexo== 'M':
        maior= idade
        nomevelho=nome
    if idade > maior and sexo =='M':
            maior= idade
            nomevelho= nome   
    if  idade<20 and sexo == 'F':
        fem+=1
media=somaidade/4
print('A media de idade do grupo é de {:.1f}'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, nomevelho))
print('Ao todo tem {} mulhere com menos de 20 anos'.format(fem))