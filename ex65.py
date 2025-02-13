from datetime import date
def voto(a):
    agora=date.today().year
    idade=agora-a
    if idade < 18:
        return f'Com {idade} anoas. NAO VOTA!'
    elif 16 <= idade >=18 or idade>65:
        return f'Com {idade} anos. O voto é OBRIGATORIO'
    else:
        return f'Com {idade} anos. O voto é OPcional'


ano=int(input('Em que ano voce nasceu? '))
print(voto(ano))
