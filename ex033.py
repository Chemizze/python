cont= mulher= homem=0
while True:
    print('  CADASTRE UMA PESSOA   ')
    id=int(input('Idade: '))
    sexo=' '
    while sexo not in 'MF':
     sexo=str(input('Sexo: [M/F] ')).upper()[0]
    tipo=' '
    while tipo not in 'SN':
     tipo=str(input('Quer continuar? [S/N] ')).upper()[0]
    if id>18:
        cont+=1
    if sexo=='M':
        homem+=1
    elif sexo=='F'and id<20:
        mulher+=1
    if tipo == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'E temos {mulher} mulheres com menos de 20 anos')