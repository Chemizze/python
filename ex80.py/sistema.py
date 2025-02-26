import index
import arquivo
from time import sleep

arq= 'cursoemvideo.txt'
if arquivo.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo nao encontrad')
    arquivo.criarArquivo(arq)

while True:
    resposta=index.menu(['Ver pessoas cadastradas', 'Cadastra nova pessoa', 'Sair do sistema'])
    if resposta ==1:
        arquivo.lerArquivo(arq)
    elif resposta ==2:
        index.cabeçalho('NOVO CADASTRO')
        nome= str(input('Nome: '))
        idade=index.leiaInt('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta==3:
        print('Saindo do sistema...')
        break
    else:
        print('\033[31mERRO: por favor digite uma opçao valida\033[m')
    sleep(2)