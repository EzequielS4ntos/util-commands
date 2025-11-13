from comandos.teste import oi

while True:
    command = input('Digite um comando: ').split(' ')

    indice = 0

    for params in command:
        if params == 'deu':
            oi(command[indice + 1])