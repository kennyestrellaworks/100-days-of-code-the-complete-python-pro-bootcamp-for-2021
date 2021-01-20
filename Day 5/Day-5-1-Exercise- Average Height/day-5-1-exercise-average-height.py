# 🚨 Don't change the code below 👇
#student_heights = input("Input a list of student heights ").split()
#for n in range(0, len(student_heights)):
#  student_heights[n] = int(student_heights[n])
## 🚨 Don't change the code above 👆
# 156 178 165 171 187


#Write your code below this row 👇
# student_heights = input("Enter a list of student heights:\n").split()

# empty = []
# sum = 0

# for x in range(0, len(student_heights)):
#   student_heights[x] = int(student_heights[x])  
#   empty.append(student_heights[x])

# for x in empty:
#   sum += x

# average = int(sum / len(empty))

# print(f"The sum is :{sum}")
# print(f"The average is :{average}")

student_heights = input("Enter a list of student heights: \n").split()
total_height = 0
number_of_students = 0

for height in student_heights:
  total_height += int(height)
  number_of_students += 1

average_height = total_height / number_of_students
average_height_rounded = round(0, 0)

print(f"The total height is: {total_height}")
print(f"The average is : {int(average_height)}")

