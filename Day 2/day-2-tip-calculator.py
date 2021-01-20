#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
bill = input("What was the total bill?\n")
tip = input("What percentage tip would you like to give? 10, 12, or 15\n")
people = input("How many people to split the bill?\n")

tip_percent = int(tip) / 100
tip_to_bill = float(bill) * tip_percent
tip_plus_bill = float(bill) + tip_to_bill
split_bill = tip_plus_bill / int(people)
final_amount = round(split_bill, 2)
final_amount = "{:.2f}".format(split_bill)
message = f"Each person should pay: {final_amount}"
print(message)