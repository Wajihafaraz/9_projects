import random 
word_list = ["python", "streamlit", "programming", "developer", "hangman"]
chosen_word=random.choice(word_list)
word_display=["_"]*len(chosen_word) #ye dash print utne karega jitne letter ka word choose hua hoaga randomly
lives = 6
guessed_letters=[]

print("Welcome to Hangman Game🎰")
print(" ".join(word_display))

while "_" in word_display and lives > 0:
    guess=input("Guess a letter: \n").lower()

    if guess in guessed_letters:
        print("you have been guess this letetr already! Enter a new letter")
        continue

    guessed_letters.append(guess)

    # ab hum for loop chalaenge
    if guess in chosen_word:
        print("✅Correct Answer ")
            #5              #5
        for i in range(len(chosen_word)):
            if chosen_word[i]== guess:
             word_display[i]=guess
    else:
       lives-=1
       print(f"❌ Wrong ! your remaining lives are {lives}") 
    print(" ".join(word_display))
    
if "_" not in word_display:
   print("\n Congratulations you win you chose right word 🎉") 

else:
   print(f"Game over😥 you lost the game. The correct word is {chosen_word}")    


