def linha (tam=42):
    return '-' *tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    print(linha())
    opc= leiaInt('\033[33mSua opçao: \033[m')
    return opc

def leiaInt(msg):
    try:
        n=int(input(msg))
    except (ValueError):
        print('\033[31mERRO: por favor. digite um numero inteiro valido\033[m')
    except:
        print('\033[31mERRO: Digite uma opçao valida\033[m')
        return 0
    else:
        return n