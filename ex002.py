num = int(input("Digite um numero inteiro: "))
print('''Escolha uma das bases para conversao: 
      [1] converter para binario
      [2] converter para octal 
      [3] converter para hexadecimal''')
opçao=int(input('Sua opçao: '))
if opçao == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para octal é igual a {}'.format(num. oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(num. hex(num)[2:]))
else:
    print('Numero invalido. opçao invalida')