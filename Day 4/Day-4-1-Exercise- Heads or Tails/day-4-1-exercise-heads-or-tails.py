#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

coin_input = input("Choose your side of the coin. Heads or Tails.\n").lower()

random_int = random.randint(0, 1)

if coin_input == "heads":
    coin_input_value = 1
elif coin_input == "tails":
    coin_input_value = 0
else:
    message = "Not specified!"

if coin_input_value == random_int:
    message = "You win!"
else:
    message = "You loose!"

print(message)

