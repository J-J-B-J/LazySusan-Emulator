import time

def delay(length):
    time.sleep(length/1000)

current_position = 0
modifier = 0
objects = {}
all_objects = {}

def list_items_on_table():
    print("\nItems on table:                           *UPDATED*")
    for obj, identifier in objects.items():
        print(" - " + obj)
    print("\n")

def print_current_position():
    print("The table is now in position " + str(current_position) + ".")
print_current_position()

def invalid_answer(user_input, error):
    print("Sorry, but '" + user_input + "' " + error)

def get_modifier():
    first_time = True
    modifier = "X"
    person = ""
    
    while modifier == "X":
        if first_time == False:
            invalid_answer(person)
        person = str(input("Who is this? "))
        first_time = False
        if person == "A":
            modifier = int(0)
            
        if person == "B":
            modifier = int(90)
                
        if person == "C":
            modifier = int(180)

        if person == "D":
            modifier = int(270)

    return modifier

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
        list_items_on_table()
        
    def unused(self):
        self.use = False
        del objects[self.name]
        list_items_on_table()


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
        miodifier = get_modifier()
        goto = input("Where to? ")
        valid_answer_found = False
        for obj, identifier in objects.items():
            if str(obj) == goto:
                identifier.goto(modifier)
                valid_answer_found = True
        if valid_answer_found == False:
            invalid_answer(goto, "wasn't on the table. The table did nothing.")


    elif action == "Remove":
        remove = input("Item to remove? ")
        found_item = False
        for obj, identifier in objects.items():
            if str(obj) == remove:
                remove = identifier
                found_item = True
        if found_item == True:
            remove.unused()
        else:
            invalid_answer(remove, "wasn't on the table.")
            list_items_on_table()
    

    elif action == "Add":
        add = input("Item to add? ")
        
        found_item = False
        for obj, identifier in all_objects.items():
            if str(obj) == add:
                correct_identifier = identifier
                found_item = True

        item_on_table = False
        for obj, identifier in objects.items():
            if str(obj) == add:
                item_on_table = True
                
        if found_item == False:
            invalid_answer(add, "dosen't exist.")
            list_items_on_table()
        elif item_on_table == True:
            invalid_answer(add, "is already on the table.")
            list_items_on_table()
        else:
            correct_identifier.used()


    else:
        invalid_answer(action)




