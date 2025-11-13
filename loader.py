import sys
import os
import urllib.request

# Mapeamento: arquivo local -> URL no GitHub
files = {
    'comandos/__init__.py': 'https://raw.githubusercontent.com/EzequielS4ntos/util-commands/main/comandos/__init__.py',
    'comandos/teste.py': 'https://raw.githubusercontent.com/EzequielS4ntos/util-commands/main/comandos/teste.py',
    'main.py': 'https://raw.githubusercontent.com/EzequielS4ntos/util-commands/main/main.py'
}

# Criar pastas e baixar arquivos
for path, url in files.items():
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    urllib.request.urlretrieve(url, path)

# Adicionar raiz do projeto ao sys.path
sys.path.insert(0, os.path.abspath('.'))

# Executar main.py
import main
