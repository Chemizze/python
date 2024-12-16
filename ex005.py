n1=float(input('Primeira nota: '))
n2=float(input('Segunda nota: '))
soma=n1+n2
media=soma/2
print('Tirando {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(n1, n2, media))
if media>=7.0:
    print('O aluno esta APROVADO')
elif media<=6.9 and media >=5.0:
    print('O aluno esta em RECUPERAÇAO')
else:
    print('O aluno esta REPROVADO')