# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
even_or_odd = number % 2
if even_or_odd > 0:
    message = f"{number} is an odd number."
else:
    message = f"{number} is an even number."
print(message)