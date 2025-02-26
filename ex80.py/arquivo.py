import index
def arquivoExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except (FileNotFoundError):
        return False
    else:
        return True
def criarArquivo(nome):
    try:
        a=open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criaçao do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
    
def lerArquivo(nome):
    try:
        a=open(nome, 'rt')
    except:
        print('ERRO ao ter o arquivo')
    else:
        index.cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())