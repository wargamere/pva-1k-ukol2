

import random

rounds = 0
wins = 0
losses = 0
draws = 0

while True:
    cislopocitac = random.randint(1, 3)
    uzivatelcislo = input("Enter rock, paper, scissors or quit:")
    rounds += 1


    if uzivatelcislo == "quit":
        print("Konec hry")
        print("Počet kol:", rounds)
        print("Počet výher:", wins)
        print("Počet proher:", losses)
        print("Počet remíz:", draws)
        if wins > losses:
            print("Vyhrál jsi")
        elif wins < losses:
            print("Prohrál jsi")
        break



    if uzivatelcislo == "rock" and cislopocitac == 1:
        print("Remíza")
        draws += 1

    elif uzivatelcislo == "paper" and cislopocitac == 2:
        print("Remíza")
        draws += 1

    elif uzivatelcislo == "scissors" and cislopocitac == 3: 
        print("Remíza")
        draws += 1





    elif uzivatelcislo == "rock" and cislopocitac == 2:
        print("Vyhrál jsi")
        print("Počítač vybral scissors")
        wins += 1

    elif uzivatelcislo == "paper" and cislopocitac == 3:
        print("Vyhrál jsi")
        print("Počítač vybral rock")
        wins += 1

    elif uzivatelcislo == "scissors" and cislopocitac == 1:
        print("Vyhrál jsi")
        print("Počítač vybral paper")
        wins += 1




    else:
        print("Prohrál jsi")
        losses += 1
        if cislopocitac == 1:
            print("Počítač vybral rock")
        elif cislopocitac == 2:
            print("Počítač vybral paper")
        else:
            print("Počítač vybral scissors")
