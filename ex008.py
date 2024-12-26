peso=float(input('Qual o seu peso?: (kg)'))
altura=float(input('Qual a sua altura?: (m)'))
i=altura **2
imc= peso/i
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc<18.5:
    print('Voce esta ABAIXO do PESO IDEAL')
elif 18.5<=imc <=25:
    print('Voce esta no PESO NORMAL')
elif 25<=imc<=30:
    print('Voce esta com SOBREPESO')
elif 30<=imc<=40:
    print('Voce esta com OBESIDADE')
else:
    print('Voce esta com OBESIDADE MORBIDA')
