# lab 3

#Task 1: Working with string
food = 'pasta'
print(food[0:3])
print(food[-3:-0])
first_last = food[0] + food[-1]
print(first_last)
food_list = food.split()
print(food_list)
joined_food = ''.join(food_list)
print(joined_food)

#task 2: working with lists
number_list = [1, 200, 524, 998, 2683 , 4387]
number_list.append(20)
print(number_list)
number_list.insert(2, 45)
number_list.pop(7)
number_list.remove(200)
print(number_list)
print(number_list[0:3])
print(number_list[3:6])

#task 3: dictionary 
books = { "Akira Toriyama" : "Dragonball" , "bryan Lee O Malley" : "scott pilgrim" , "Atushi Ohkubo" : "Soul Eater", "Katherine Patterson" : "Bridge to Terabithia"}
x = books.keys()
print(x)
y = books.values()
print(y)
z = books.get("Atushi Ohkubo")
print(z)
books.pop("Atushi Ohkubo")
print(books)
books = { "Akira Toriyama" : "Dragonball" , "bryan Lee O Malley" : "scott pilgrim" , "Atushi Ohkubo" : "Soul Eater", "Katherine Patterson" : "Bridge to Terabithia"}
del books["Akira Toriyama"]
print(books)

