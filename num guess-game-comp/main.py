import random
# Guess the Number Game Python Project (computer)

def main():
    secret_num = random.randint(1,100)

    while True:
        user_num = int(input("Guess a number: "))

        if user_num > secret_num:
            print("Your guessing number is too high!Enter a new num..")

        elif user_num < secret_num:
            print("Your guessing number is too low! Enter a new one..")

        else:
            print("🎉Congrats! you guess a correct number!")  
            break  
        
main()        