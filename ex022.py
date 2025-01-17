sexo=str(input('Degite o seu sexo [M/F]: '))
while sexo not in 'MmFf':
    sexo=str(input('Dados invalidos. Por favor, informe seu sexo[M/F]: '))
print('O teu sexo {} registrado com sucesso'.format(sexo))