# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()
name_combo = name1_lowercase + name2_lowercase
true = ["t","r","u","e",]
love = ["l","o","v","e"]

with_true = []
with_love = []

for x in true:
  with_true.append(name_combo.count(x))
with_true_sum = sum(with_true)

for x in love:
  with_love.append(name_combo.count(x))
with_love_sum = sum(with_love)

result_combine = str(with_true_sum) + str(with_love_sum)
result_combine_int = int(result_combine)

if result_combine_int < 10 or result_combine_int > 90:
  message = f"Your score is {result_combine_int}, you go like coke & mentos."
elif result_combine_int > 40 and result_combine_int < 50:
  message = f"Your score is {result_combine_int}, you are alright together."
else:
  message = f"Your score is {result_combine_int}."
print(message)