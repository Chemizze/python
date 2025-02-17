c=('\033[m', '\033[0;30;41m')
def ajuda(com):
    help(com)
def titulo(msg, cor=0):
    print(c[cor], end='')
    tan=len(msg)+4
    print('~'*tan)
    print(f'  {msg}')
    print('~'*tan)
    print(c[0], end='')


comando=''
while True:
    titulo('SiSTEMA DE AJUDA PyHELP', 1)
    comando=str(input('Funçao ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo')