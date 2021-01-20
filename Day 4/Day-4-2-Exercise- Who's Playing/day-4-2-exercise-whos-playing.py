import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_len = len(names) - 1
random_number = random.randint(0, names_len)
print("Random number is ", random_number)
print("Names len is", names_len)
will_pay = names[random_number]
print(f"{will_pay} will pay for the meal today!")
