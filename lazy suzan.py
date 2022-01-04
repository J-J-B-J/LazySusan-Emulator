import time #The time library is used to wait in between long chunks of text

current_position = 0    #Set the # of degrees the table has turned = 0

#The modifier is used when the table needs to turn to face an item to a person.
#Each person has a modifier that is added to the current position to calculate
#how much to turn.
modifier = 0

objects = {}    #Contains the objects and their identifiers that are on the table.
all_objects = {}    #Contains all the objects and their identifiers.


#This function prints out all the objects in turn
#It's used when a change to the objects dictionary occurs
def list_items_on_table():  
    print("\nItems on table:        *UPDATED*")  #Say what is printed below
    for obj, identifier in objects.items(): #For each obj & id in objects
        print(" - " + obj)  #Print name of object in bullet point format
    print("\n") #Print new line at the end

def print_current_position(): #This function prints table's current position
    print("The table is now in position " + str(current_position) + ".")
print_current_position()    #Run the above function upon program run

def invalid_answer(user_input, error):  #Print an error message
    print("Sorry, but '" + user_input + "' " + error)

def get_modifier(): #This function returns the modifier for the specified user
    first_time = True   #The below while loop is on the first iteration
    modifier = "X"  #So that if the input isn't A/B/C/D, the program will know
    person = "" #Create the variable person outside of the while loop scope
    
    while modifier == "X":  #While the person hasn't given a straight andswer
        if first_time == False: #If this is the 2nd+ iteration,
            invalid_answer(person, "is not a valid answer.")  #Give an error
        person = str(input("Who is this? "))    #Set person to user input
        first_time = False  #This is now not the first iteration
        if person == "A":   #If the user input is A
            modifier = int(0)   #Then set the modifier to A's modifier
            
        if person == "B":
            modifier = int(90)
                
        if person == "C":
            modifier = int(180)

        if person == "D":
            modifier = int(270)

    return modifier #Return the modifier once the user has given a valid answer

#This class is for real-world objects that can be placed on the lazy susan
class table_object:
    def __init__(self, name, pos, use):
        #Name, Position on table, Currently on table?
        self.name = name
        self.position = pos
        self.use = use
        
        #Add this object to the all_objects dictionary
        all_objects[self.name] = self

    #Goto turns table so that the chosen item is facing the chosen person
    def goto(self, modifier):
        global current_position #So that goto can change that table's position
        print("Going to " + self.name + ".")    #Say where the table should go
        time.sleep(1)

        turn = (self.position + modifier) - current_position    #Calculate turn
        current_position = (current_position + turn) % 360  #Update pos var

        #The following converts turns greater than 180 into negative numbers
        #E.g. 260 turn becomes -100 turn
        if(turn > 180):
            turn = (360 - turn) * -1
            
        if(turn < 0):
            #Print the turn as anticlockwise
            print("The table turned " + str(turn*-1) + " anticlockwise.")
        if(turn > 0):
            #Print the turn as clockwise
            print("The table turned " + str(turn) + " clockwise.")
        if(turn == 0):  #i.e. table is already in correct position
            print("The table did not move.")    #Print the turn as nothing
        time.sleep(1)
        print_current_position()    #Show the table's updated position
        time.sleep(1)

    def used(self): #This function enables the item
        self.use = True #Enable in object
        objects[self.name] = self   #Enable in objects dictionary
        list_items_on_table()   #Print updated table items
        
    def unused(self):   #This function disables the item
        self.use = False    #Disable in object
        del objects[self.name]  #Disable in objects dictionary
        list_items_on_table()   #Print updated table items


#These are the objects that can be enabled:
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
    action = str(input("Enter action: "))   #Ask what the user wants to do

    
    if action == "Goto":    #If the user wants to turn the table:
        miodifier = get_modifier()  #Get the modifier for a specific person
        goto = input("Where to? ")  #Ask what item the person wants
        valid_answer_found = False  #The user hasn't yet provided valid answer
        for obj, identifier in objects.items(): #Repeat w all objects on table
            #If the item the user entered matches a table object
            if str(obj) == goto:
                identifier.goto(modifier)   #Turn table to the table object
                valid_answer_found = True
        if valid_answer_found == False: #If the item asked for didn't exist
            invalid_answer(goto, "wasn't on the table. The table did nothing.")


    elif action == "Remove":    #If the user wants to disable an item:
        remove = input("Item to remove? ")  #Ask for an item
        found_item = False  #The user hasn't yet provided a valid answer yet
        for obj, identifier in objects.items(): #Repeat w all objects on table
            #If the item the user entered matches a table object
            if str(obj) == remove:
                remove = identifier #Set remove to the object to remove
                found_item = True
        if found_item == True:
            remove.unused() #Disable the item
        else:
            invalid_answer(remove, "wasn't on the table.")
            list_items_on_table()   #Show updated list
    

    elif action == "Add":   #If the user wants to enable an item
        add = input("Item to add? ")    #Ask for an item
        
        found_item = False  #The user hasn't yet provided a valid answer yet
        for obj, identifier in all_objects.items(): #Repeat w all objects on table
            #If the item the user entered matches a table object
            if str(obj) == add:
                correct_identifier = identifier #Set to the object to remove
                found_item = True

        #This code figures out weather or not the item ia already on the table
        item_on_table = False
        for obj, identifier in objects.items():
            if str(obj) == add:
                item_on_table = True
 
        if found_item == False: #If the item dosen't exist       
            invalid_answer(add, "dosen't exist.")   #Error
            list_items_on_table()
        elif item_on_table == True: #If the item is on the table
            invalid_answer(add, "is already on the table.") #Error
            list_items_on_table()
        else:   #If the item is valid
            correct_identifier.used()   #Enable the item


    else:   #If the action provided isn't valid
        invalid_answer(action, "isn't a valid action.")




