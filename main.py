from metods.hello import hello
import os

os.system('cls')
os.system('color 02')

print('===== teste =====')

while True:
    command = input('> ')

    if command == 'hello':
        os.system('cls')
        name = input('Insira seu nome\n> ')