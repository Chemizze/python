from random import randint
n=(randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Eu sortiei os valores {n}')
s=sorted(n)
print(f'O maior valor é {s[-1]}')
print(f'O menor valor é {s[0]}')