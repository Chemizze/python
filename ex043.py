lista=[]
mai=men=0
for c in range(0, 5):
    n=int(input('Digite um valor: '))
    if c==0 or  n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        pos =0
        while pos < len(lista):
            if n <=lista[pos]:
              lista.insert(pos, n)
              print(f'Adiconado na posiçao {pos} da lista')
              break
print('-='*30)
print(f'Os valores digitador na ordem foram {lista}')