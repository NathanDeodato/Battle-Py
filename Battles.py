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
    shooter = [55, 36, 8, 12]
    wizard = [60, 28, 12, 16]
    assassin = [65, 30, 14, 26]
    
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

            sleep(2)

            menoslife1 = 26 - 20
            fighting_paladin = life_paladin - menoslife1
            life_paladin = fighting_paladin
            
            print(branco + "- Attack Warrior -".center(150))
            print(vermelho + f"Paladin: -{menoslife1}HP".center(150))
            print(verde + f"Paladin: {life_paladin}HP".center(150))

            sleep(2)

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
    if player == 2 and machine == 3 or player == 3 and machine == 2:
        print(cinza + "=" * 150)

        life_paladin = 90
        life_shooter = 55

        power_paladin = [20, 26, 6]
        power_shooter = [36, 8, 12]

        while life_paladin > 0 or life_shooter > 0:
            print(branco + f"-- {rounds}ª Round --".center(150))
            print(cinza + "-" * 150)

            rounds+=1

            sleep(2)

            menoslife1 = 36 - 26
            fighting_paladin = life_paladin - menoslife1
            life_paladin = fighting_paladin

            print(branco + "- Attack Shooter -".center(150))
            print(vermelho + f"Paladin: -{menoslife1}HP".center(150))
            print(verde + f"Paladin: {life_paladin}HP".center(150))

            sleep(2)

            menoslife2 = 20 - 8
            fight_shooter = life_shooter - menoslife2
            life_shooter = fight_shooter

            print(branco + "- Attack Paladin -".center(150))
            print(vermelho + f"Shooter: -{menoslife1}HP".center(150))
            print(verde + f"Shooter: {life_shooter}HP".center(150))

            print(cinza + "-" * 150)

            sleep(2)

            if life_paladin <= 0:
                break
            elif life_shooter <= 0:
                break

    ### Shooter vs Wizard
    if player == 3 and machine == 4 or player == 4 and machine == 3:
        print(cinza + "=" * 150)

        life_shooter = 55
        life_wizard = 60

        power_shooter = [36, 8, 12]
        power_wizard = [28, 12, 16]

        while life_shooter > 0 or life_wizard > 0:
            print(branco + f"-- {rounds}ª Round --".center(150))
            print(cinza + "-" * 150)

            rounds+=1

            sleep(2)

            menoslife1 = 28 - 8
            fight_shooter = life_shooter - menoslife1
            life_shooter = fight_shooter

            print(branco + "- Attack Wizard -".center(150))
            print(vermelho + f"Shooter: -{menoslife1}HP".center(150))
            print(verde + f"Shooter: {life_shooter}HP".center(150))

            sleep(2)

            menoslife2 = 36 - 12
            fight_wizard = life_wizard - menoslife2
            life_wizard = fight_wizard

            print(branco + "- Attack Shooter -".center(150))
            print(vermelho + f"Wizard: -{menoslife2}HP".center(150))
            print(verde + f"Wizard: {life_wizard}HP".center(150))

            print(cinza + "-" * 150)

            sleep(2)

            if life_shooter <= 0:
                break
            if life_wizard <= 0:
                break

    ### Wizard vs Assassin
    if player == 4 and machine == 5 or player == 5 and machine == 4:
        print(cinza + "=" * 150)

        life_wizard = 60 
        life_assassin = 65

        power_wizard = [26, 12, 16]
        power_assassin = [30, 14, 26]

        while life_wizard > 0 or life_assassin > 0:
            print(branco + f"-- {rounds}ª Round --".center(150))
            print(cinza + "-" * 150)

            rounds+=1

            sleep(2)

            menoslife1 = 30 - 12
            fight_wizard = life_wizard - menoslife1
            life_wizard = fight_wizard

            print(branco + "- Attack Assassin -".center(150))
            print(vermelho + f"Wizard: -{menoslife1}HP".center(150))
            print(verde + f"Wizard: {life_wizard}HP".center(150))

            sleep(2)

            menoslife2 = 28 - 14
            fight_assassin = life_assassin - menoslife2
            life_assassin = fight_assassin

            print(branco + "- Attack Wizard -".center(150))
            print(vermelho + f"Assassin: -{menoslife2}HP".center(150))
            print(verde + f"Assassin: {life_assassin}HP".center(150))

            print(cinza + "-" * 150)

            sleep(2)

            if life_assassin <= 0:
                break
            elif life_wizard <= 0:
                break

    ### Assassin vs warrior
    if player == 5 and machine == 1 or player == 1 and machine == 5:
        print(cinza + "=" * 150)

        life_assassin = 65
        life_warrior = 80

        power_assassin = [30, 14, 26]
        power_warrior = [26, 20, 22]

        while life_assassin > 0 and life_warrior > 0:
            print(branco + f"-- {rounds}ª Round --".center(150))
            print(cinza + "-" * 150)

            rounds+=1

            sleep(2)

            menoslife1 = 30 - 20
            fight_warrior = life_warrior - menoslife1
            life_warrior = fight_warrior

            print(branco + "- Attack Assassin -".center(150))
            print(vermelho + f"Warrior: -{menoslife1}HP".center(150))
            print(verde + f"Warrior: {life_warrior}HP".center(150))

            sleep(2)

            menoslife2 = 26 - 14
            fight_assassin = life_assassin - menoslife2
            life_assassin = fight_assassin

            print(branco + "- Attack Warrior -".center(150))
            print(vermelho + f"Assassin: -{menoslife2}HP".center(150))
            print(verde + f"Assassin: {life_assassin}HP".center(150))

            print(cinza + "-" * 150)
            
            sleep(2)

            if life_assassin <= 0:
                break
            elif life_warrior <= 0:
                break

    ### Warrior vs Shooter
    if player == 1 and machine == 3 or player == 3 and machine == 1:
        print(cinza + "=" * 150)

        life_warrior = 80
        life_shooter = 55

        power_warrior = [26, 20, 22]
        power_shooter = [36, 8, 12]

        while life_warrior > 0 or life_shooter > 0:
            print(branco + f"-- {rounds}ª Round --".center(150))
            print(cinza + "-" * 150)

            rounds+=1

            sleep(2)

            menoslife1 = 26 - 8
            fight_shooter = life_shooter - menoslife1
            life_shooter = fight_shooter

            print(branco + "- Attack Warrior -".center(150))
            print(vermelho + f"Shooter: -{menoslife1}HP".center(150))
            print(verde + f"Shooter: {life_shooter}HP".center(150))

            sleep(2)

            menoslife2 = 36 - 20
            fight_warrior = life_warrior - menoslife2
            life_warrior = fight_warrior

            print(branco + "- Attack Shooter -".center(150))
            print(vermelho + f"Warrior: -{menoslife1}HP".center(150))
            print(verde + f"Warrior: {life_warrior}HP".center(150))

            print(cinza + "-" * 150)

            sleep(2)

            if life_warrior <= 0:
                break
            elif life_shooter <= 0:
                break

    ### Paladin vs wizard
    if player == 2 and machine == 4 or player == 4 and machine == 2:
        print(cinza + "=" * 150)

        life_paladin = 90
        life_wizard = 60

        power_paladin = [20, 26, 6]
        power_wizard = [28, 12, 16]

        while life_paladin > 0 or life_wizard > 0:
            print(branco + f"-- {rounds}ª Round --".center(150))
            print(cinza + "-" * 150)

            rounds+=1

            sleep(2)

            menoslife1 = 28 - 26
            fight_paladin = life_paladin - menoslife1
            life_paladin = fight_paladin

            print(branco + "- Attack Wizard -".center(150))
            print(vermelho + f"Paladin: -{menoslife1}HP".center(150))
            print(verde + f"Paladin: {life_paladin}HP".center(150))

            sleep(2)

            menoslife2 = 20 - 12
            fight_wizard = life_wizard - menoslife2
            life_wizard = fight_wizard

            print(branco + "- Attack Paladin -".center(150))
            print(vermelho + f"Wizard: -{menoslife2}HP".center(150))
            print(verde + f"Wizard: {life_wizard}HP".center(150))

            print(cinza + "-" * 150)

            sleep(2)

            if life_paladin <= 0:
                break
            elif life_wizard <= 0:
                break

    ### Wizard vs Warrior

    ### Paladin vs Assassin
