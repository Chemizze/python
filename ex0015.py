soma =0
cont = 0
for c in range (1, 7):
    num = int (input('Digite o {} numero: '.format(c)))
    if num % 2 ==0:
        soma += num
        cont += 1
print('Voce informou {} e a soma dos pares foi {}'.format(cont, soma))
        
