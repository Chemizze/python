from datetime import date
atual = date.today().year
nasc= int(input('Ano de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade ==18:
    print('Voce tem que se alistrar imediatamente ')
elif idade <18:
    saldo = 18 - idade
    print('Ainda falta {} anos para o alistamento.'.format(saldo))
    ano= atual + saldo
    print('O teu alistamento sera em {} anos'.format(ano))
elif idade >18:
    saldo=  idade - 18
    print(input('Voce ja deveria ter se alistrado ha {} anos'.format(saldo)))
    ano= atual - saldo
    print('Voce deveria ter se alistado ha {} anos'.format(ano))
