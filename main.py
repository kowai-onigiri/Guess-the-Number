import random
import art
from replit import clear


def game():
  #---------Logo----------
  print(art.logo)
  
  #----------Number Generator----------
  random_num = random.randint(1,100)
  # print(random_num) #testing purposes

  #----------Difficulty Selector----------
  def select_difficulty():
    difficulty = input("Select your difficulty: easy or hard \n").lower()

    if difficulty == "easy":
      difficulty = "easy_mode"
      return difficulty
    elif difficulty == "hard":
      difficulty = "hard_mode"
      return difficulty
    else:
      print("Invalid input. Please try again.")

  difficulty = select_difficulty()
  if difficulty == None:
    game()
  else:
    if difficulty == "easy_mode":
      print(" ")
      print("You selected easy mode.")
      num_guess = 10
    else:
      print(" ")
      print("You selected hard mode.")
      num_guess = 5
    # print(f"Difficulty: {difficulty}")
    print(" ")
    print(f"Number of guesses: {num_guess}")
    print(" ")

  #---------Game Round----------
  
  def play_round():
    print("=====================================")
    print(" ")
    lives = num_guess
    game_end = False
    

    while game_end == False:
      player_guess = int(input("Guess a number: \n"))

      
      
      if player_guess == random_num:
        print(" ")
        print(art.win)
        print(" ")
        game_end = True
      elif player_guess > random_num:
        print(" ")
        print("Too high! Guess again.")
        print(" ")
        print("=====================================")
        print(" ")
        print(f"Guesses left: {lives}")
        print(" ")
        
        lives -= 1
        if lives == 0:
          game_end = True
      else:
        print(" ")
        print("Too low! Guess again.")
        lives -= 1
        if lives == 0:
          game_end = True
        print(" ")
        print("=====================================")
        print(" ")
        print(f"Guesses left: {lives}")
        print(" ")
      
      
    if lives == 0:
      print(art.lose)
      print(" ")

    
  play_round()
game()

play_again = True


while play_again == True:
  another_game = input("Do you want to play again? \n").lower()

  if another_game == "yes":
    clear()
    game()
  else:
    clear()
    print(art.goodbye)
    play_again = False
  
  
  

