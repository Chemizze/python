matriz=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma=soma1=mai=0
for l in range(0,3):
    for c in range(0,3):
       matriz[l][c]=int(input(f'Digite um valor [[{l}],[{c}]]: '))
       
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c]%2==0:
          soma+=matriz[l][c]
        if c==2:
            soma1+=matriz[l][2]

    print()
    
print('-='*30)   
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da terceira coluna é {soma1}')
for c in range(0, 3):
    if c==0:
        mai = matriz[1][c]
    elif mai < matriz[1][c]:
            mai = matriz[1][c]
print(f'O valore maior da segunda linha é {mai}')