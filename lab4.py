checking = "yes"

while checking == "yes":
    input("what is your age: ")
    user_input = input()
    if int(user_input) >= 18:
        print("yes you can vote")
    else: 
        print("no you cant vote")
    print("would you like to check another age")
    user_input2 = input()
    checking = user_input2

list1 = [3, -1, 0, 6, -4]
for x in list1:
    if x > 0:
        print("value is positive")
    elif x < 0:
        print("value is negative")
    elif x == 0:
        print("value is zero")

        
invetory = ["coal," "dirt", "diamond", "gravel", "stone"]
for item in invetory:
    print("stone")
for i in invetory:
    if i == "diamond":
        print("Jackpot!")
