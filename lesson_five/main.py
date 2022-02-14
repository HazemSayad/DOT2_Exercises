# Lesson 5 Practice Hands-On created by the one and only Hazem

# Part 1
# variables

# functions
def sum_function(x,y,z):
    return x+y+z

def product_function(x,y,z):
    return x*y*z

def average_function(x,y,z):
    return sum_function(x,y,z) / 3.0

print(sum_function(10,80,2))
print(product_function(25,42,2))
print(average_function(6,8,1))


# Part 2
# variables


# functions
add_numbers = lambda x,y,z: x+y+z
multiply_numbers = lambda x,y,z: x*y*z
average_numbers = lambda x,y,z: (x+y+z)/3.0

print(add_numbers(10,80,2))
print(multiply_numbers(25,42,2))
print(average_numbers(6,8,1))


# Part 3
# variables
list_one = [4,6,88,24]
list_two = [17,34,9,5]
list_three = [63,20,98,4]

# functions
average_maker = lambda x,y,z: (x+y+z)/3.0

map_results = map(average_maker,list_one,list_two,list_three)
print(list(map_results))

# no funny or joke comments, move along please, nothing to see here