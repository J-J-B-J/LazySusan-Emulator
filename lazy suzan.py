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
            turn = turn * -1
            print("The table turned " + str(turn) + " degrees anticlockwise.")
        else:
            print("The table turned " + str(turn) + " degrees clockwise.")
        delay(1000)
        print_current_position()
        delay(1000)


bible = table_object("Bible", 0)
fruit = table_object("Fruit", 0)
desert = table_object("Desert", 0)


objects = {
    "Bible": bible,
    "Fruit": fruit,
    "Desert": desert


while True:
    action = str(input("Enter action: "))
    
    if action == "goto":
        person = str(input("Who is this? "))
        
        if person == "J":
            modifier = int(0)
            
        if person == "G":
            modifier = int(90)
            
        if person == "B":
            modifier = int(180)

        if person == "A":
            modifier = int(270)

        print("Modifier: " + str(modifier))

        goto = input("Where to? ")

        for obj, identifier in objects.items():
            if str(obj) == goto:
                identifier.goto(modifier)
