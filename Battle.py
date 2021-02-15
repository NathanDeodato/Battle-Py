# Libs
from Battles import Battles
from random import randint

# Colors
ciano = "\033[1;96m"
vermelho = "\033[1;31m"
branco = "\033[1;32m"
branco = "\033[1;97m"

# Start
print(ciano + "=" * 150)
print(branco + "-- Battle-Game --".center(150))
print(ciano + "=" * 150)

print(branco + "Esse é um jogo de batalha, com uma mecanica de batalhas por rodada.")
print(branco + "Está preparado para jogar contra mim? Sou sua máquina. Hehehe")
print(branco + "VAMOS LÁ!")


while True:
    try:
        print(ciano + "=" * 150)
        
        print(branco + "Selecione sua classe de guerreiro")
    
        print(ciano + "-" * 150)

        print(branco + "[ 1 ] Warrior")
        print("[ 2 ] Paladin")
        print("[ 3 ] Shooter")
        print("[ 4 ] Wizard")
        print("[ 5 ] Assassin")

        print(ciano + "=" * 150)

        player = int(input(branco + "Selecione a classe: "))
        while player != 1 and player != 2 and player != 3 and player != 4 and player != 5:
            player = int(input(branco + "Selecione a classe: "))
        
        machine = 2
        #machine = randint(1, 5)

        Battles(player, machine)

        print(ciano + "=" * 150)
        
        print(branco + "[ 1 ] Sim")
        print(branco + "[ 2 ] Não")

        print(ciano + "-" * 150)

        go = int(input(branco + "Continue? "))
        
        if go == 2:
            print(ciano + "=" * 150)
            print(branco + "-- Battle-Close --".center(150))
            print(ciano + "=" * 150)

            break

    except Exception as erro:
        print(vermelho + "Erro: {erro}")

