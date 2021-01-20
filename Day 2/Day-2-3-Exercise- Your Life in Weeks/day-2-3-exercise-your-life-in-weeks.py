# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days_per_year = 365
weeks_per_year = 52
months_per_year = 12
age_limit = 90

remaining_years = age_limit - int(age)
remaining_days = remaining_years * days_per_year
remaining_weeks = remaining_years * weeks_per_year
remaining_months = remaining_years * months_per_year

message = f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left."
print(message)