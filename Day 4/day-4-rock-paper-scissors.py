import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to rock, paper & scissors game!")
print("To select type the following:")
print("R for rock\nP for paper\nS for scissors")

def play_again_game():
  print("********************************")
  play_again = input("Wanna play again? Y / N:\n")
  play_again_lowercase = play_again.lower()
  if play_again_lowercase == "y":
    init()
  elif play_again_lowercase == "n":
    print("Game ends!")
  else:
    print("Choice not specified.")
    play_again_game()

def game_play(random_number, player_hand):  
  if player_hand == random_number:
    print("********************************")
    play_again = input("It's a draw! Wanna play again? Y / N\n")
    play_again_lowercase = play_again.lower()
    if play_again_lowercase == "y":
      init()
    elif play_again_lowercase == "n":
      print("Game ends!")
    else:
      print("Choice not specified.")
      play_again_game()
  else:
    if player_hand == 0:
      if random_number == 1:
        print("********************************")
        print(f"You loose!\n{rock} is defeated by {paper}")
      elif random_number == 2:
        print("********************************")
        print(f"You win!\n{rock} defeats {scissors}")
    elif player_hand == 1:
      if random_number == 0:
        print("********************************")
        print(f"You win!\n{paper} defeats {rock}")
      elif random_number == 2:
        print("********************************")
        print(f"You loose!\n{paper} is defeated by {scissors}")
    elif player_hand == 2:
      if random_number == 0:
        print("********************************")
        print(f"You loose!\n{scissors} is defeated by {rock}")
      elif random_number == 1:
        print("********************************")
        print(f"You win!\n{scissors} defeats {paper}")
  play_again_game()

def generate_random_number():
  random_number = random.randint(0, 2)
  return random_number

def play_again():
  init()

def init():
  random_number = generate_random_number()
  print("********************************")
  player_hand = input("Choose your hand:\n")
  player_hand_lowercase = player_hand.lower()
  if player_hand_lowercase == "r":
    player_hand = 0
  elif player_hand_lowercase == "p":
    player_hand = 1
  elif player_hand_lowercase == "s":
    player_hand = 2
  else:
    print("Wrong input.")
    play_again()
  game_play(random_number, player_hand)

init()