#Write your code below this row 👇
# for number in range(1, 11):
#   if number % 2 == 0:
#     print(number)

total = 0
for number in range(1, 101):
  if number % 2 == 0:
    total += number

print(f"The sum of all even number from 1 to 100 is: {total}")
