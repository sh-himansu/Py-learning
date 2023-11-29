print("Welcome to roller coster ride")

height = int(input("Enter your height in cm:\n"))

if height >= 120:
    print("You are eligible for roller coster ride")
    age = int(input("Enter your age\n"))
    if age < 18:
        price = 5
        print("You have to pay $5")
    elif age >=18 and age <=25:
        price = 10
        print("You have to pay $10")
    elif age > 25 and age <=40:
        price = 12
        print("You have to pay $12")
    elif age > 40  and age <=50:
        price = 0
        print("You are free of charges")
    photos = input("If you want to take a photo during the ride Y or N\n")
    if photos == "Y":
        price= price+3
    print(f"Your total bill is {price}")
else:
    print("Your height is not sufficient to ride")