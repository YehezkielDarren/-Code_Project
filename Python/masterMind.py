import random

def mastermind():
    print("{:=^30}".format("MASTERMIND GAME"))
    #rule
    rule=["Rules :","1. Bot will automaticly picking random number in range 1,000 to 10,000",
          "2. User's task is to guessing the number",
          "3. If Player 2 succeeds in his first attempt (despite odds which are highly unlikely) he wins the game and is crowned Mastermind!",
          "4. If not, then bot hints by revealing which digits or numbers user got correct.",
          "5. The game continues till user eventually is able to guess the number entirely.",
          "6. Mastermind is when u can guess the number maximum in three attempts"]
    for i in rule:
        print(i)
    #game begin
    while True:
        #computer pick
        computer_pick=random.randrange(1000,10000)
        user_guess=[]
        for _ in str(computer_pick):
            user_guess.append("X")
        print_guess="".join(user_guess)
        print(print_guess)
        #user guess
        userpick=int(input("Input number within range 1000 to 10000 : "))

mastermind()