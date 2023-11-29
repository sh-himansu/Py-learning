print("Welcome to BMI calculator")
weight = int(input("Enter your weight in KG\n"))
height = float(input("Enter your height in meter\n"))

bmi = weight / height **2

print(f"Your BMI is {bmi}")