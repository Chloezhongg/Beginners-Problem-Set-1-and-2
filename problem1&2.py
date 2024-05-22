###1. Convert Minutes into Seconds

minutes = int(input("Enter the number of minutes: "))
seconds = minutes * 60
print(f"{seconds} seconds")

###2. Jane's Birthday Cards

cruella_cards = int(input("Enter the number of cards Cruella received: "))
jane_cards = cruella_cards * 2
print(f"Jane receives at least {jane_cards} cards.")

###3. Age to Days

age_in_years = int(input("Enter your age in years: "))
days_old = age_in_years * 365
print(f"You are {days_old} days old.")
3.1 Expand Age to Days with Days to 100 Years Old
python
Copy code
age_in_years = int(input("Enter your age in years: "))
days_old = age_in_years * 365
days_to_100 = (100 - age_in_years) * 365
print(f"You are {days_old} days old. In {days_to_100} days you will be 100 years old!")
