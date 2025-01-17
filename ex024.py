num=int(input('Primeiro valor: '))
num1=int(input('Segundo valor: '))
opçao= 0
while opçao != 5:
   
    print('''        [1] somar
        [2] multiplicar
        [3] maior
        [4] novos numeros
        [5] sair do programa ''')
    opçao=int(input('>>> Qual é a sua opçao? ')) 
    if opçao==1:
        soma=num+num1
        print('A soma entre {} + {} é {}'.format(num, num1, soma))
    elif opçao==2:
        mult=num*num1
        print('A multiplicaçao entre {} e {} é {}'.format(num, num1, mult))
    elif opçao==3:
        if num > num1:
            print('O maior numero é {}'.format(num))
        elif num1 > num:
            print('O maior numero é {}'.format(num1))
    elif opçao==4:
        num=int(input('Primeiro valor: '))
        num1=int(input('Segundo valor: '))
    
    
    
print('ACABOU')   
        