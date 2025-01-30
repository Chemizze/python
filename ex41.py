palavra=('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')
for c in palavra:
    print(f'\n Na palavra {c} temos', end =' ')
    for letras in c:
        if letras.lower() in 'aeiou':
            print(letras, end=' ')