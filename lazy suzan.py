import time

def delay(length):
    time.sleep(length/1000)

current_position = 0
modifier = 0
objects = {}
all_objects = {}

def print_current_position():
    print("The table is now in position " + str(current_position) + ".")
print_current_position()

class table_object:
    def __init__(self, name, pos, use):
        self.name = name
        self.position = pos
        self.use = use
        all_objects[self.name] = self

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

    def used(self):
        self.use = True
        objects[self.name] = self
        
    def unused(self):
        self.use = False
        del objects[self.name]


cutlery = table_object("Cutlery", 0, False)
tom_sauce = table_object("Tomato Sauce", 0, False)
bbq_sauce = table_object("BBQ Sauce", 0, False)
chilli_sauce = table_object("Sweet Chilli Sauce", 0, False)
salad = table_object("Salad", 0, False)
salt = table_object("Salt", 0, False)
pepper = table_object("Pepper", 0, False)
bible = table_object("Bible", 0, False)
olive_oil = table_object("Olive Oil", 0, False)

while True:
    action = str(input("Enter action: "))

    
    if action == "Goto":
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


    if action == "Remove":
        remove = input("Item to remove? ")
        
        for obj, identifier in objects.items():
            if str(obj) == remove:
                remove = identifier
        remove.unused()
    

    if action == "Add":
        add = input("Item to add? ")
        
        for obj, identifier in all_objects.items():
            if str(obj) == add:
                identifier.used()


    if action == "List":
        print("\n\nAll items:\n")
        print(all_objects)
        print("\n\nUsed items:\n")
        print(objects)
        print("\n\n")




