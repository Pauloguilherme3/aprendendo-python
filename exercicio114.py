import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu Erro site fora do ar')
else:
    print('Site funcionando normalmente')
