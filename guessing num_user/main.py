#Guess the Number Game Python Project (user)
#you will build a guessing game where the computer has to guess the correct number. 
import random

def comp_guess():

    low = 1 
    high = 100

    print ("Think a number between 1 to 100 then computer guess your number.")

    while True:
        comp_guess=random.randint(low,high)
        feedback = input(f"Is my guess number {comp_guess} is high , low or correct.")

        if feedback == "high":
            high = comp_guess - 1  #50 -1 =49

        elif feedback == "low":
            low = comp_guess + 1 # 40 + 1 =41

        elif feedback == "correct":
            print(f"Congratulations you guess the right num!")  
            break
        else:
            print("Invalid input only write high, low or correct.")      


comp_guess()
         




