#1
def cat_greeting(word):
    print(f"cat says {word}")
    print("cat says nothing")
cat_greeting("meow")

#2
def generate_superhero_power():
    name = "bob"
    power = "flying" 
    print(f"{name}'s power is {power}")
generate_superhero_power()

#3
def generate_superhero_power1():
    power = "flying"
    return power
print(generate_superhero_power1)
#4
def generate_superhero_power2(user_name, super_power):
    message = user_name +  "has the power of "   + super_power + "!"
    return message
print(generate_superhero_power2("bob,",  "flying"))

#5
def cat_greetings_loop(hello):
    for i in range(5):
        print(f" the cat says {hello}") 
cat_greetings_loop("meow")

#6
def generate_multiple_powers(power):
    for i in (power):   
        print(i)

power_tests = ("flying", "invisibility", "super strength")
generate_multiple_powers(power_tests)


 

