# # 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇
##############################################
# [2, 10, 1, 5, 12, 3, 5]
# [1, 2, 5, 8, 23, 30, 25, 23, 25, 30]
# [3, 10, 25, 61, 4, 8, 7, 9, 10, 66, 7, 61, 52]
list_items = [3, 10, 25, 61, 4, 8, 7, 9, 10, 66, 7, 61, 52]

higher_number_index = 0
lesser_number_index = 0

higher_number_count = 0
lesser_number_count = 0

# Highest number.
# We will compare the value inside the list_items using it's indices (item) where we get
# the index of the value that is greater than or less than. We store the index of the value
# that is higher to higher_number_index. Using higher_number_count enables us to add 1 so that 
# we can move to the next index when the loop runs.
for item in list_items:
  # Default, when we are at the first item of the list. The higher_number_index will have
  # the index of the first item of list_items.
  if int(list_items[higher_number_index]) == int(list_items[higher_number_count]):
    higher_number_index = higher_number_count
  # When the value represented by higher_number_index is greater than the value
  # represented by higher_number_count.
  elif int(list_items[higher_number_index]) > int(list_items[higher_number_count]):
    higher_number_index = higher_number_index
  # When the value represented by higher_number_index is less than the value
  # represented by higher_number_count. 
  elif int(list_items[higher_number_index]) < int(list_items[higher_number_count]):
    higher_number_index = higher_number_count
  higher_number_count += 1

for item in list_items:
  if int(list_items[lesser_number_index]) == int(list_items[lesser_number_count]):
    lesser_number_index = lesser_number_count
  elif int(list_items[lesser_number_index]) > int(list_items[lesser_number_count]):
    lesser_number_index = lesser_number_count
  elif int(list_items[lesser_number_index]) < int(list_items[lesser_number_count]):
    lesser_number_index = lesser_number_index
  lesser_number_count += 1

print(f"The highest number is: {list_items[higher_number_index]}")
print(f"The lowest number is : {list_items[lesser_number_index]}")

##############################################
# number_list = [10, 2, 32, 31, 8, 23, 30, 25, 23, 25, 30]

# highest_number = 0

# for number in number_list:
#   if number > highest_number:
#     highest_number = number
# print(f"The highest number is: {highest_number}")