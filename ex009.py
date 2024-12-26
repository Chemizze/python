preço=float(input('Qual o preço da compra:$'))
print('''Qual a forma de pagamento?
      [1] Dinheiro/cheque
      [2] à vista Cartao
      [3] 2x no cartao
      [4] 3x ou mais no cartao''')
opçao=int(input('Qual a opçao'))
if opçao==1:
   total = preço - (preço * 10/100)
   print('Sua campra de ${:.2f} vai custar ${:.2f} no final'.format(preço. total))
elif opçao==2:
    total= preço -(preço * 5/100)
    print('Sua compra de ${:.2f} vai custar ${:.2f} no final'.format(preço, total))
elif opçao==3:
    print('O sua preço sera ${:.2f} no final'.format(preço))
elif opçao==4:
    total=preço+(preço*20/100)
    per=int(input('Quantas parcelas?: '))
    parcela= total/per
    print('Sua compra sera parcelada em {}x de de ${:.2f} com juros'.format(per, parcela))
    print('Sua compra de ${:.2f} vai custar {:.2f} no final'.format(preço, total))
