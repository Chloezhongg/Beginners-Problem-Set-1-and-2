####problem1
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
age_in_years = int(input("Enter your age in years: "))
days_old = age_in_years * 365
days_to_100 = (100 - age_in_years) * 365
print(f"You are {days_old} days old. In {days_to_100} days you will be 100 years old!")

####problem2
def mad_libs():
    print("Welcome to Mad Libs!")
    
    name = input("What is your name? ")
    adjective = input("Enter an adjective (describing word): ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    food = input("Enter a food: ")
    vehicle = input("Enter a vehicle: ")
    
    story = (
        f"{name} is a very {adjective} person to be around. "
        f"They love to {verb} in {place}. "
        f"Their favourite food is {food} which they eat in a {vehicle}."
    )
    
    print("\n" + story)

mad_libs()
