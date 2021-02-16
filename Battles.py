# Libs
from time import sleep

# Colors
cinza = "\033[1;90m"
vermelho = "\033[1;31m"
verde = "\033[1;32m"
branco = "\033[1;97m"


# Def Battle
def Battles(player, machine):
    print(cinza + "=" * 150)
    
    ## Attributs
    warrior = [80, 26, 20, 22]
    paladin = [90, 20, 26, 6]
    shooter = [50, 28, 8, 12]
    wizard = [60, 26, 12, 16]
    assassin = [70, 30, 14, 26]
    
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

    print(branco + "-- Class --".center(150))
    print(f"Player: {info_player}")
    print(f"Machine: {info_machine}")

    ## Combats
    rounds = 1

    print(cinza + "=" * 150)
    print(branco + "-- → FIGHT ← --".center(150))

    ### Warrior vs paladin
    if player == 1 and machine == 2 or player == 2 and machine == 1:
        print(cinza + "=" * 150)
        
        life_warrior = 80
        life_paladin = 90

        power_warrior = [26, 20, 22]
        power_paladin = [20, 26, 6]

        while life_warrior > 0 or life_paladin > 0:
            print(branco + f"-- {rounds}ª Round --".center(150))
            print(cinza + "-" * 150)
            
            rounds+=1

            menoslife1 = 26 - 20
            fighting_paladin = life_paladin - menoslife1
            life_paladin = fighting_paladin
            
            print(branco + "- Attack Warrior -".center(150))
            print(vermelho + f"Paladin: -{menoslife1}HP".center(150))
            print(verde + f"Paladin: {life_paladin}HP".center(150))

            sleep(1)

            menoslife2 = 0
            fighting_warrior = life_warrior - menoslife2
            life_warrior = fighting_warrior

            print(branco + "- Attack Paladin -".center(150))
            print(vermelho + f"Warrior: -{menoslife2}HP".center(150))
            print(verde + f"Warrior: {life_warrior}HP".center(150))

            sleep(2)
            print(cinza + "-" * 150)

            if life_warrior <= 0:
                break
            if life_paladin <= 0:
                break

    ### Paladin vs Shooter

    ### Shooter vs Wizard

    ### Wizard vs Assassin

    ### Assassin vs warrior

    ### Warrior vs Shooter

    ### Paladin vs wizard

    ### Wizard vs Warrior

    ### Paladin vs Assassin

    ### Assassin vs Warrior
