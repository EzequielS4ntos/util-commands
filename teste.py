import sys
import os
import urllib.request

# Baixar arquivo do GitHub
url = 'https://raw.githubusercontent.com/EzequielS4ntos/util-commands/main/comandos/teste.py'
os.makedirs('comandos', exist_ok=True)
urllib.request.urlretrieve(url, 'comandos/teste.py')

# Adicionar pasta comandos ao sys.path
sys.path.append(os.path.abspath('comandos'))

# Agora dá para importar
from teste import oi

oi()
