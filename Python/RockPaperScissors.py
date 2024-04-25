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