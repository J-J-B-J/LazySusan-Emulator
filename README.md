# Lazy-Susan Emulator and Driver
A motorised lazy Susan Emulator and Driver

This repository is based on the AIY Voice Kit. (https://aiyprojects.withgoogle.com/voice/) Based on Raspberry Pi, this kit helps with voice recognition. The goal of this repo is to make a motorised lazy Susan that you can use voice commands to control.

## This repository contains 2 files:
The first file is a program that is a text-based emulator of a motorised lazy Susan. Since I am yet to make a functioning lazy Susan, in the meantime I have made this program. It asks who is requesting the item, then what item they want, then reports back what the table is doing.

The second file is a program that is to be used with a voice kit. WARNING: This program is currently untested. I do not currently own a Voice Kit or have a functioning lazy Susan.
### PLEASE DO NOT USE THE SECOND PROGRAM
It has never been tested. The second program will be tested and used once I acquire a Voice Kit and find a way to move the lazy Susan with electronics

# UPDATES

---
### UPDATE: V1.1
- Issue resolved: When the table should only turn anticlockwise, it turns clockwise and anticlockwise
---
### UPDATE: V1.2
- You can now "Enable" or "Disable" table objects if you take them off your lazy Susan
---
### UPDATE: V1.3
- The code for getting the modifier for each person is now a function
- The program checks for validity whenever it asks for user input
- Prints an appropriate error message upon invalid user input
- Prints the items that are on the table whenever there is a change to them
---
### UPDATE: V1.4
- All old delay functions changed to Python Standard time.sleep
- More comments added
- All lines longer than 79 characters shortened
---
### UPDATE: V1.5
- Add and Remove functions combined into one action
- Tests and assertions added
- Code for get_modifier function turned into dictionary
---
### UPDATE V1.6
- Ability to turn the table manually using "Turn" action
- Achieved PEP 8 compliance
- "Edit" command renamed "Toggle"
- Change position of an item during the run using the new "Edit" action
- When you enable an item, the program will automatically run the "Edit" command.
---
### UPDATE V1.7
- New lazy susan class
- "Cancel" command exits the action you're running
- PEP 8 compliance maintained
- More comments added to tests
---
### COMING SOON
- Custom items able to be placed on table
- People's names
- Try-Except-Else blocks
- Settings kept in .json file
