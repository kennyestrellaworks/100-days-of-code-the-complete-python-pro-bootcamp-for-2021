# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?\n")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
empty = []

for x in position:
    empty.append(x)

empty_len = len(empty)
if empty_len <= 2:
    row_item = int(empty[0])
    column_item = int(empty[1])
if row_item <= 3 and column_item <= 3:
    map[column_item - 1][row_item - 1] = "x"
    print(f"{row1}\n{row2}\n{row3}")
else:
    print("Position not covered.")
else:
    print("Position not covered.")

#Write your code above this row 👆

# 🚨 Don't change the code below 👇