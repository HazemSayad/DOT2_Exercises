# Lesson 4 Hands-On created by the one and only Hazem

# Part 1 

# variables
pets = {
    'Max': {
        'Type': 'Dog',
        'Color': 'Radiant Uranium-Green',
        'Nickname': 'Maxi',
        'Ownername': 'Chernobyl'
    },
    'Lex': {
        'Type': 'Cat',
        'Color': 'Bright Nuclear Mushroom Cloud',
        'Nickname': 'Lilly',
        'Ownername': 'Hiroshima'
    }
}

# get the keys and use them, can be simplified more by changing first loop to pets.values(), but i chose this method for general purposes for my reasons
for petKeyName in pets:
    for petKey in pets.get(petKeyName):
        print(petKey + ": " + pets.get(petKeyName).get(petKey))


# Part 2

# variables
england = {'Capital': 'London'}
france = {'Capital': 'Paris'}
belgium = {'Capital': 'Brussels'}

# adding population to dict
england['population'] = '53.01 million'
france['population'] = '66.9 million'
belgium['population'] = '11.35 million'

# adding interesting totally real facts
england['fact'] = 'England is itself!'
france['fact'] = 'France has an evil tower!' # not eiffel tower; also fake facts
belgium['fact'] = 'Belgium has humans, cats and dogs in it!'

# adding language spoken
england['lang'] = 'English and Chinese'
france['lang'] = 'Chinese and Egnlish'
belgium['lang'] = 'Chenglish'  # you think i am power tripping by creating things in my own creations, well you are correct and i am having a blast!

# print(england)
# print(france)
# print(belgium)


# Part 3

# variables
pizza_order = {
    'customerName': 'Bill Gates',
    'pizzaSize': 'Extra Large',
    'crust': 'Cheesy',
    'toppings': ('cheese','pepper','pineapples')  # yeah, pinapples go on pizza and can legally still call it pizza, deal with it
}

print("Thank you for your order, " + pizza_order.get('customerName') + " You have ordered a " + pizza_order.get('pizzaSize') + ", " + pizza_order.get('crust') + "-crust pizza with the following toppings: " + str(pizza_order.get('toppings')))