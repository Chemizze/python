print('-'*30)
print('      LOJA SUPER BARATÃO         ')
print('-'*30)
cont=conta=menor=soma=0
while True:
    produto=str(input('Nome do Produto: ' ))
    preço=float(input('Preço: R$'))
    continuar=' '
    while continuar not in 'SN':
        continuar=str(input('Quer continuar? [S/N] ')).split()[0]
    soma=soma+preço
    if preço>1000:
        cont+=1
    if conta ==1:
        menor = preço
        barato = produto
    else:
        if preço < menor:
            menor = preço
            barato = produto
    if continuar=='N':
        break
print('{:.-⁴40}'.format(' Fim do PROGRAMA '))
print(f'O total da compra foi {soma:.2f}')
print(f'Temos {cont} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa {menor:.2f}')    