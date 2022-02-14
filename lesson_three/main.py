# Lesson 3 Practice Hands-On by the one and only Hazem

# Part 1
# variables

list_of_names = ['Kurt','David','Katherine']

for name in list_of_names:
    print("Where is",name,"today?")


# Part 2
# variables

my_favorite_cars = ['BMW','Tesla','Smart']
my_favorite_flowers = ['Tulip','Rose','Lotus','Lily Pond']
my_favorite_animals = ['Cheetah','Cat','Dog','Mouse','Elephant']
my_favorite_things = []

for car in my_favorite_cars:
    my_favorite_things.append(car)

for flower in my_favorite_flowers:
    my_favorite_things.append(flower)

for animal in my_favorite_animals:
    my_favorite_things.append(animal)

for thing in my_favorite_things:
    if len(thing) % 2 == 0:
        print(thing)


# Part 3
# variables

number_range = list(range(1,21))

# i think the below algorithm is probably faster than going through bunch of and/or's. Didnt test speed, sp i ended up with this cute little thing down below!
for number in number_range:
    if number % 3 == 0:
        if number % 5 == 0:
            print("ZipZap")
        else:
            print("Zip")
    elif number % 5 == 0:
        print("Zap")
    else:
        print(number)
