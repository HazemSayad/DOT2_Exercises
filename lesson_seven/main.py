# Lesson 7 Practice Hands-On created by the one and only Hazem

from datetime import datetime

# Part 1

# variables
todaysDate = datetime.now()
timeNow = datetime.time(datetime.now())  # i can easily pass the above variable, but i wanted to trigger it twice to see the time difference between each line, pretty fast i must say!

print("Today is:",todaysDate,"\nTime:", timeNow)


# Part 2

# variables
poem_string = "Tiny little secrets\nGet buried in the dirt,\nAnd if they were dug up,\nSomeone would probably get hurt."

with open('poem.txt', 'w') as poem_file:
    poem_file.write(poem_string)

with open('poem.txt','r') as poem_file:
    print(poem_file.read())