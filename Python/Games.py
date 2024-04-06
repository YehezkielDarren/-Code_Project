import random
def RockPapScis():
    print("--ROCK PAPPER SCISSORS GAME--")
    user_Scores=0
    bot_Scores=0
    options=['rock','paper','scissors']
    round=1
    #rock = 0; paper = 1; scissors = 2
    while True:
        print(f"Round {round}.")
        round+=1    
        users_Input=input("Type Rock(R)/Paper(P)/Scissors(S) or Q to quit : ").lower()
        number=random.randint(0,2)
        bot_Input=options[number]
        if users_Input=="q":
            break
        if users_Input not in ["rock",'paper','scissors','r','p','s']:
            continue
        print(f"Computer pick '{bot_Input}'.")
        if users_Input=="r" and bot_Input=="scissors":
            user_Scores+=1
            print("You Win")
        elif users_Input=="r" and bot_Input=="paper":
            bot_Scores+=1
            print("You Lose")
        elif users_Input=="p" and bot_Input=="scissors":
            bot_Scores+=1
            print("You Lose")
        elif users_Input=="p" and bot_Input=="rock":
            user_Scores+=1
            print("You Win")
        elif users_Input=="s" and bot_Input=="paper":
            user_Scores+=1
            print("You Win")
        elif users_Input=="s" and bot_Input=="rock":
            bot_Scores+=1
            print("You Lose")
    win= None
    if user_Scores>bot_Scores:
        win="You Win"
    elif user_Scores<bot_Scores:
        win="You Lose"
    elif user_Scores==bot_Scores:
        win="Duece"
    print(f"Bot Scores : {bot_Scores} || User Scores : {user_Scores}\n'{win}'")        
    print("The Game Stop")
def hangman():
    print("--HANGMAN GAME--")
    lives=10
    #given words
    words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"
                 ]
    while True:
        chosen_word=random.choice(words).lower()
        user_input=None #character that user input each round (only 1 character)
        temp_words=[]
        word_guessed=[] #place the each correct character that user input
        for _ in chosen_word:
            word_guessed.append("_")
            
        while (lives!=0)and("_" in word_guessed):
            print("=========================")
            print(f"You has {lives} HP left")
            displaying_guess="".join(word_guessed)
            print(displaying_guess)
            print("=========================")
            try:
                user_input=input("Type one word 'a-z' or 'esc' to quit : ").lower()
                print("=========================")   
            except:
                print("Invalid Input. Try Again!!")
                continue
            else:
                if  not user_input.isalpha() or len(user_input)!=1:
                    if user_input=="esc":
                        main()
                    print("Invalid Input. Try Again!!")
                    continue
                elif user_input in word_guessed:
                    print(f"This word '{user_input}' has already guessed by user, Try Again !")
                    continue
            if (user_input in chosen_word):
                for i in range(len(chosen_word)):
                    if user_input in chosen_word[i]:
                        word_guessed[i]=user_input
            elif (user_input not in chosen_word):
                if user_input in temp_words:
                    print(f"Wrong Guessed and You Alredady Guess It")
                    lives-=1
                else:
                    temp_words.append(user_input)
                    print(f"Wrong guess !!")
                    lives-=1
                continue
            
        if "_" not in word_guessed:
            print(f"You Win, CONGRATSSS!!!\nLife Remaining : {lives} HP left")
            play_again=input("Do You Want To Play Again ?").lower()
            if play_again not in ("yes","y","true","t"):
                quit()
            else:
                main() 
            
        if ("_" in word_guessed) and lives==0:
            print("You lose !!!")
            print(f"The answer is : '{chosen_word}'.")
            play_again=input("Do You Want To Play Again ?").lower()
            if play_again not in ("yes","y","true","t"):
                quit()
            else:
                main()                        
def TicTaToe():
    pass
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
                        main()
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
                        main()
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
                        main()

def main():
    print("Python Games")
    print("=====================")
    print("Choose :")
    print("1. Rock-Paper-Scissors")
    print("2. Hang Man")
    print("3. Tic Tac Toe 'Still Developed' ")
    print("4. Number Guessing")
    print("5. -")
    print("=====================")
    options=int(input("Input the number list : "))
    if options==1:
        print()
        RockPapScis()
    elif options==2:
        print()
        hangman()
    elif options==3:
        print("Under Developement, Coming Soon!!")
        main()
    elif options==4:
        print()
        numberGuessing()
    else:
        print("There is no game available, try again!!")
        main()

if __name__=='__main__':
    main()