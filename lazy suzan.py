import time

def delay(length):
    time.sleep(length/1000)

current_position = 0
modifier = 0
objects = {}

def print_current_position():
    print("The table is now in position " + str(current_position) + ".")
print_current_position()

class table_object:
    def __init__(self, name, pos):
        self.name = name
        self.position = pos

    def goto(self, modifier):
        global current_position
        print("Going to " + self.name + ".")
        delay(1000)
        turn = (self.position + modifier) - current_position

        current_position = (current_position + turn) % 360
        
        if(turn > 180):
            turn = (360 - turn) * -1
            
        if(turn < 0):
            print("The table turned " + str(turn*-1) + " degrees anticlockwise.")
        if(turn > 0):
            print("The table turned " + str(turn) + " degrees clockwise.")
        if(turn == 0):
            print("The table did not move.")
        delay(1000)
        print_current_position()
        delay(1000)


cutlery = table_object("Cutlery", 0)
sauce = table_object("Sauce", 90)
desert = table_object("Desert", 270)


objects = {
    "Cutlery": cutlery,
    "Sauce": sauce,
    "Desert": desert,
}

while True:
    action = str(input("Enter action: "))
    
    if action == "goto":
        person = str(input("Who is this? "))
        
        if person == "A":
            modifier = int(0)
            
        if person == "B":
            modifier = int(90)
            
        if person == "C":
            modifier = int(180)

        if person == "D":
            modifier = int(270)

        goto = input("Where to? ")

        for obj, identifier in objects.items():
            if str(obj) == goto:
                identifier.goto(modifier)
