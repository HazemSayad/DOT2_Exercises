# Lesson 6 Hands-On created by the one and only Hazem

# Part 1

class Stadium:
    "This is a Lesson 6 hands on class named Stadium"

    def __init__(self, name, city_state, capacity):
        
        """        
        Init function for Stadium class

        Accepted parameter for name (String), city_state (String), capacity (Num/Str)
        """

        self.name = name
        self.city_state = city_state
        self.capacity = capacity
    
    def describe_stadium(self):
        print("The " + self.name + " is located in " + self.city_state + " and holds " + str(self.capacity) + " fans.")


# Part 2

    def sport_played(self, sport_played):

        "Accepted parameter for sport_played (String)"

        self.sport_played = sport_played
        print("The following sport is mainly played in this stadium: " + self.sport_played)
    
    def seats_available(self, available_seats):

        "Accepted parameter for available_seats (Num/Str)"

        self.available_seats = available_seats
        print("There are " + str(self.available_seats) + " seats still available for tonight's game.")


stadium1 = Stadium("Merc Benz Arena", "Atlanta, GA", 70000)
stadium1.describe_stadium()

stadium1.sport_played("Football")
stadium1.seats_available(15000)

# and you thought i will be putting a joke somewhere in this code, HA! thats what i call a practical prank! I am on a race here with myself to become an excellent programmer. With dedication, hard work, and sweat and tears (maybe some blood!)