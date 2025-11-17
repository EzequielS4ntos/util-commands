from metods.hello import hello
from time import sleep
import os

os.system('cls')
os.system('color 02')

def digite(text, time = 0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(time)

msg = 'Script de serviço iniciado'
msg2 = 'Seja bem vindo'

digite(msg)

digite('...', 1)

sleep(3)

os.system('cls')

digite(msg2)

sleep(2)

os.system('cls')

while True:
    command = input('> ')

    if command == 'hello':
        os.system('cls')
        name = input('Insira seu nome\n> ')
        print(hello(name))

    
    if command == 'exit':
        break

    if command == 'cls' or command == 'clear':
        os.system('cls')