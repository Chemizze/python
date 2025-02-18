def metade(n=0, formato=False):
    res= n/2
    return res if formato is False else moeda(res)
def dobro(n=0, formato=False):
    res= n*2
    return res if formato is False else moeda(res)
def aumentar(n=0, p=1, formato=False):
    res= n+(n/p)
    return res if formato is False else moeda(res)
def diminuir(n=0, p=1, formato=False):
    res= n-(n/p)
    return res if formato is False else moeda(res)
def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
def resumo(n=0, pa=10, pd=5):
    
    print(f'-'*30)
    print('        RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro analisado: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{pa}% de aumento: \t{aumentar(n, pa, True)}')
    print(f'{pd}% de reduçao: \t{diminuir(n, pd, True)}')
    print(f'-'*30)
    