def metade(n=0):
    res= n/2
    return res
def dobro(n=0):
    res= n*2
    return res
def aumentar(n=0, p=0):
    res= n+(n/p)
    return res
def diminuir(n=0, p=0):
    res= n-(n/p)
    return res
def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')