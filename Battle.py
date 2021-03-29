# Libs
from Battles import Battles
from random import randint
from time import sleep

# Colors
cinza = "\033[1;90m"
vermelho = "\033[1;31m"
branco = "\033[1;97m"

# Start
print(cinza + "=" * 150)
print(branco + "-- Battle-Game --".center(150))
print(cinza + "=" * 150)

print(branco + "Esse é um jogo de batalha, com uma mecanica de batalhas por rodada.")
print(branco + "Está preparado para jogar contra mim? Sou sua máquina. Hehehe")
print(branco + "VAMOS LÁ!")

sleep(1)


while True:
    try:
        print(cinza + "=" * 150)
        
        print(branco + "Selecione sua classe de guerreiro")
    
        print(cinza + "-" * 150)

        sleep(1)

        print(branco + "[ 1 ] Warrior")
        print("[ 2 ] Paladin")
        print("[ 3 ] Shooter")
        print("[ 4 ] Wizard")
        print("[ 5 ] Assassin")

        sleep(1)

        print(cinza + "=" * 150)

        player = int(input(branco + "Selecione a classe: "))
        while player != 1 and player != 2 and player != 3 and player != 4 and player != 5:
            player = int(input(branco + "Selecione a classe: "))
        
        machine = 5
        #machine = randint(1, 5)

        ## Infs Battle
        info_player = ""
        info_machine = ""

        if player == 1:
            info_player = "Warrior"
        elif player == 2:
            info_player = "Paladin"
        elif player == 3:
            info_player = "Shooter"
        elif player == 4:
            info_player = "Wizard"
        elif player == 5:
            info_player = "Assassin"

        if machine == 1:
            info_machine = "Warrior"
        elif machine == 2:
            info_machine = "Paladin"
        elif machine == 3:
            info_machine = "Shooter"
        elif machine == 4:
            info_machine = "Wizard"
        elif machine == 5:
            info_machine = "Assassin"

        # Empate
        if player == machine:
            print(branco + "-- Class --".center(150))
            print(f"Player: {info_player}")
            print(f"Machine: {info_machine}")
            
            print(cinza + "=" * 150)

            print(branco + "- Select again! -".center(150))

        else:
            Battles(player, machine)

        print(cinza + "=" * 150)
        
        sleep(1)

        print(branco + "[ 1 ] Sim")
        print(branco + "[ 2 ] Não")

        print(cinza + "-" * 150)

        sleep(1)

        go = int(input(branco + "Continue? "))
        
        if go == 2:
            sleep(1)

            print(cinza + "=" * 150)
            print(branco + "-- Battle-Close --".center(150))
            print(cinza + "=" * 150)

            break

    except Exception as erro:
        print(vermelho + f"Erro: {erro}")

