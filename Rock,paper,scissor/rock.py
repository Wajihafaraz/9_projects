import random


def rock_paper_scissor():

 choices=["Rock" , "Paper", "Scissor", ]

 while True:
  user_choice = input("Choose rock, paper , scissor: ").lower

  if user_choice != choices:
   print("Invalid choice, choose only rock , paper and scissor.")

   comp_choice=random.choice(choices)
   print(f"Computer choose: {comp_choice}")

   if user_choice == comp_choice:
    print("Its a tie, try again!")

  elif (user_choice == "rock" and comp_choice == "scissor"):
   print(f"You win the game 😃 because rock beats the scissor")

  elif (user_choice == "paper" and comp_choice == "rock"):
   print(f"You win the game 😃 because paper beats the rock")

  elif (user_choice == "scissor" and comp_choice == "paper"):
   print(f"You win the game 😃 because scissor beats the paper")

  else:
   print("You lose!😥 and Computer wins the game🎉")
   
  play_again=input("Do you want to play again? (yes / no ): ").lower

  if play_again != "yes":
   print("Thanks for playing! 🎮")
