import random

input("Welcome to Rock, Paper and Scissors! Press enter to start ")

user_score = 0
cpu_score = 0

while True:
 print()
 user_choice = input("Pick an option between R, P or S: ").lower()

 while user_choice != "r" and user_choice != "p" and user_choice != "s":
  user_choice = input("Invalid input, please try again: ").lower()

 random_num = random.randint(0,2)
 if random_num == 0:
  cpu_choice = "r" 
 elif random_num == 1:
  cpu_choice = "p"
 elif random_num == 2:
  cpu_choice = "s"

 print()
 print("Your choice: ", user_choice)
 print("Computer's choice: ", cpu_choice)
 print()

 if user_choice == "r":
  if cpu_choice == "r":
   print("It's a tie!")
  elif cpu_choice == "p":
   print("You lost!")
   cpu_score += 1
  elif cpu_choice == "s":
   print("You win!")
   user_score += 1
   
 elif user_choice == "p":
  if cpu_choice == "p":
   print("It's a tie!")
  elif cpu_choice == "s":
   print("You lost!")
   cpu_score += 1
  elif cpu_choice == "r":
   print("You win!")
   user_score += 1

 elif user_choice == "s":
  if cpu_choice == "s":
   print("It's a tie!")
  elif cpu_choice == "r":
   print("You lost!")
   cpu_score += 1
  elif cpu_choice == "p":
   print("You win!")
   user_score += 1
 
 print()
 print("You have", user_score, "wins")
 print("The Computer has", cpu_score, "wins")
 print()

 repeat = input("Play again? (Y/N) ").lower()
 while repeat != "n" and repeat !="y":
  repeat = input("Invalid input, please try again: ").lower()

 if repeat == "n":
  break
 print("\n----------------------------------------------------\n")
