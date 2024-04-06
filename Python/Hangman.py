import random

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
                        quit()
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
                hangman() 
            
        if ("_" in word_guessed) and lives==0:
            print("You lose !!!")
            print(f"The answer is : '{chosen_word}'.")
            play_again=input("Do You Want To Play Again ?").lower()
            if play_again not in ("yes","y","true","t"):
                quit()
            else:
                hangman()