from comandos.teste import oi

while True:
    command = input('Digite um comando: ')

    command.split(' ')

    indice = 0

    for params in command:
        if params == 'teste':
            oi(command[indice + 1])