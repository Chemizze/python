lista=[]
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posiao {c}: ')))
print('='*50)
print(f'Voce digitou os valores {lista}')  
print(f'O maior valor digitado foi {max(lista)}')
print(f'O menor valor digitado foi {min(lista)}')