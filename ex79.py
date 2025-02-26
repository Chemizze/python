import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim,com,br')
except:
    print('O site nao esta acessivel')
else:
    print('Tudo ok')