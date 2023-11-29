print("Welcome to py-love calculator")

name1= input("Enter your name:\n")
name2= input("Enter your partner's name\n")

combine_name = name1+name2

lower_name = combine_name.lower()
T = lower_name.count("t")
R = lower_name.count("r")
U = lower_name.count("u")
E = lower_name.count("e")

L = lower_name.count("l")
O = lower_name.count("o")
V = lower_name.count("v")
E = lower_name.count("e")

result1 = str(T+R+U+E)
result2 = str(L+O+V+E)

final = result1+result2

print(f"Your love percentage is {final}")
