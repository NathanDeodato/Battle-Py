# Libs
from time import sleep

# Colors
cinza = "\033[1;90m"
vermelho = "\033[1;31m"
verde = "\033[1;32m"
preto = "\033[1;30m"


# Def Battle
def Battles(player, machine):
    ## Attributs
    warrior = [100, 26, 20, 22]
    paladin = [100, 20, 26, 6]
    shooter = [100, 28, 8, 12]
    wizard = [100, 26, 12, 16]
    assassin = [100, 30, 14, 26]
    
    ## Combats
    ### Warrior vs paladin
    if player == 1 and machine == 2 or player == 2 and machine == 1:
        life_warrior = 100
        life_paladin = 100

        power_warrior = [26, 20, 22]
        power_paladin = [20, 26, 6]

        print("-- Warrior attack first --".center(150))

        while life_warrior > 0 or life_paladin > 0:
            menoslife1 = 20 - 20
            fighting_paladin = life_paladin - menoslife1
            life_paladin = fighting_paladin
            
            print("-Attack Warrior-")
            print(f"Paladin: -{menoslife1}HP")
            print(f"Paladin: {life_paladin}HP")

            sleep(2)

            menoslife2 = 20 - 26
            fighting_warrior = life_warrior - menoslife2
            life_warrior = fighting_warrior

            print("-Attack Paladin-")
            print(f"Warrior: -{menoslife2}HP")
            print(f"Warrior: {life_warrior}HP")

            sleep(2)

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
