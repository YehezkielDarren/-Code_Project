import random

def numberGuessing():
    print("--Number Guessing--")
    freeBalance_eachNewGame=1
    mode=["h","m","e","hard","medium","easy"]
    yes_no=["y","n"]
    while freeBalance_eachNewGame%5!=0:
        freeBalance_eachNewGame= random.randint(100,5_000)
    print(f"Your Balance : ${freeBalance_eachNewGame:,}")
    print("================================")
    #Rules Of The Game
    rules=["Rules : ","1. At the beginning of the game, you will get free balance (Randomly Generated)",
           "2. Your task is to guess what is the mystery number",
           "3. You will be given several chances to guess (the number of chances is based on your bet amount)",
           "4. If your guess is wrong, your chances will be reduced by one",
           "5. If your guess is correct, you win the game and you will get the prize based on rules",
           "6. Prize amount based each difficulty",
           "7. Each difficulties have different maximum chances"]
    for i in rules:
        print(i)
    print("================================")
    tempBalance=freeBalance_eachNewGame
    while True:
        #Difficulty
        while True:
            try:
                diff=input("Select The Difficulty 'Hard(H)'/'Medium(M)'/'Easy(E)' : ").lower()
            except IOError:
                print("Your Input Doesn't Match With The Rules, Try Again!!")
                continue
            else:
                if diff not in mode:
                    print("Your Input Doesn't Match With The Rules, Try Again!!\n")
                    continue
                elif diff in mode:
                    print()
                    break                 
        #Game Begin
        while True:
            #Easy Mode
            if diff=="e" or diff=="easy" :
                chances=7 #attempts for easy mode
                print("{:=^30}".format("EASY MODE"))
                print("Prizepool = (Your bet x 50%) x chances left")
                print()
                while True:
                    placeBet=int(input("Put Your Bet (min $.20): $"))
                    if placeBet<20:
                        print("Your Bet is too low, try again!!\n")
                        continue
                    else:
                        tempBalance-=placeBet
                        print()
                        break
                print("You must guess a number between 1-100\n")
                #computer picking some number
                computerPick=random.randint(1,100)
                while chances!=0:
                    print(f"Your chances is {chances}")
                    try:
                        userPick=int(input("Guess a number 1-100 : "))
                    except IOError:
                        print("Not a Number, try again!!\n")
                        continue
                    else:
                        if userPick<computerPick:
                            print("Wrong Guess!! Too low\n")
                            chances-=1
                            continue
                        elif userPick>computerPick:
                            print("Wrong Guess!! Too High\n")
                            chances-=1
                            continue
                        else:
                            prize_pool=(placeBet*0.5)*chances
                            tempBalance+=prize_pool
                            print(f"\nYou win!!\nCongrats, you got ${prize_pool:,}")
                            print(f"Your Balance Now : $.{tempBalance:,}\n")
                            break
                if chances==0 and userPick!=computerPick:
                    print(f"You Lose!!\nThe Number Is : {computerPick}\nYour Balance Now : $.{tempBalance:,}\n")
                while True:
                    try:
                        play_again=input("Want Play More Game ? (Y/N) : ").lower()
                    except IOError:
                        print("Invalid Input, try again!!\n")
                        continue
                    else:
                        if play_again not in yes_no:
                            continue
                        else:
                            break
                if play_again in yes_no:
                    if play_again==yes_no[0]:
                        print("{:=^30}".format("New Game"))
                        break
                    else:
                        print()
                        quit()
            #medium mode        
            elif diff=="m" or diff=="medium":
                chances=7 #attempts for medium mode
                print("{:=^30}".format("MEDIUM MODE"))
                print("Prizepool = (Your bet x 70%) x chances left")
                print()
                while True:
                    placeBet=int(input("Put Your Bet (min $.35): $"))
                    if placeBet<35:
                        print("Your Bet is too low, try again!!\n")
                        continue
                    else:
                        tempBalance-=placeBet
                        print()
                        break
                print("You must guess a number between 1-400\n")
                #computer picking some number
                computerPick=random.randint(1,400)
                while chances!=0:
                    print(f"Your chances is {chances}")
                    try:
                        userPick=int(input("Guess a number 1-400 : "))
                    except IOError:
                        print("Not a Number, try again!!\n")
                        continue
                    else:
                        if userPick<computerPick:
                            print("Wrong Guess!! Too low\n")
                            chances-=1
                            continue
                        elif userPick>computerPick:
                            print("Wrong Guess!! Too High\n")
                            chances-=1
                            continue
                        else:
                            prize_pool=(placeBet*0.7)*chances
                            tempBalance+=prize_pool
                            print(f"\nYou win!!\nCongrats, you got $.{prize_pool:,}")
                            print(f"Your Balance Now : $.{tempBalance:,}\n")
                            break
                if chances==0 and userPick!=computerPick:
                    print(f"You Lose!!\nThe Number Is : {computerPick}\nYour Balance Now : $.{tempBalance:,}\n")
                while True:
                    try:
                        play_again=input("Want Play More Game ? (Y/N) : ").lower()
                    except IOError:
                        print("Invalid Input, try again!!\n")
                        continue
                    else:
                        if play_again not in yes_no:
                            continue
                        else:
                            break
                if play_again in yes_no:
                    if play_again==yes_no[0]:
                        print("{:=^30}".format("New Game"))
                        break
                    else:
                        print()
                        quit()
            #Hard Mode
            elif diff=="h" or diff=="hard":
                chances=6 #attempts for hard mode
                print("{:=^30}".format("HARD MODE"))
                print("Prizepool = (Your bet x 90%) x chances left")
                print()
                while True:
                    placeBet=int(input("Put Your Bet (min $.100): $"))
                    if placeBet<100:
                        print("Your Bet is too low, try again!!\n")
                        continue
                    else:
                        tempBalance-=placeBet
                        print()
                        break
                print("You must guess a number between 1-600\n")
                #computer picking some number
                computerPick=random.randint(1,600)
                while chances!=0:
                    print(f"Your chances is {chances}")
                    try:
                        userPick=int(input("Guess a number 1-600 : "))
                    except IOError:
                        print("Not a Number, try again!!\n")
                        continue
                    else:
                        if userPick<computerPick:
                            print("Wrong Guess!! Too low\n")
                            chances-=1
                            continue
                        elif userPick>computerPick:
                            print("Wrong Guess!! Too High\n")
                            chances-=1
                            continue
                        else:
                            prize_pool=(placeBet*0.9)*chances
                            tempBalance+=prize_pool
                            print(f"\nYou win!!\nCongrats, you got $.{prize_pool:,}")
                            print(f"Your Balance Now : $.{tempBalance:,}\n")
                            break
                if chances==0 and userPick!=computerPick:
                    print(f"You Lose!!\nThe Number Is : {computerPick}\nYour Balance Now : $.{tempBalance:,}\n")
                while True:
                    try:
                        play_again=input("Want Play More Game ? (Y/N) : ").lower()
                    except IOError:
                        print("Invalid Input, try again!!\n")
                        continue
                    else:
                        if play_again not in yes_no:
                            continue
                        else:
                            break
                if play_again in yes_no:
                    if play_again==yes_no[0]:
                        print("{:=^30}".format("New Game"))
                        break
                    else:
                        print()
                        quit()
