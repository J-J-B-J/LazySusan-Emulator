# Lazy-Susan Emulator

This program is a text-based emulator of a motorised lazy Susan. Since I am yet to make a functioning lazy Susan, in the meantime I have made this program. It asks who is requesting the item, then what item they want, then reports back what the table is doing.

# Instructions
If you have items saved from last time, the program will first ask you if you want to restore them.

Please note that the program automatically interprets all user input in title case.

After this, the program will prompt you with "Action: ". There are six actions you can perform:
- "Turn"
- "Toggle"
- "Bulk Toggle"
- "Goto"
- "Edit"
- "Users"
- "Clear"
- "Preset"
- "Edit Presets"

### Turn
The turn function is the most basic. Enter an integer, (positive or negative,) and the emulated lazy susan will turn that much. Note that is you enter a turn greater than 359 or less than -359, the program will continue adding or subtracting until the turn is within the above range. E.g. You enter "370", the table turns 10.

### Toggle
Toggle either enables or disables an item. While using toggle, enter an item. If the item is already enabled, the program will disable it. If there is no enabled item called this, the program will make and enable a new one.

In real life, enable is the equivalent of putting an item on the lazy susan, and disable is the equivalent of taking an item off.

When you have toggled an item, the program will print an updated list of items on the table.

### Bulk Toggle
Bulk toggle is the same as "Toggle," except the program keeps asking for items until you enter "Cancel."

### Goto
When an item is enabled, you can run goto for the susan to bring it to you.

After entering your name, enter the item you want brought to you. The program will report what is happening.

### Edit
The Edit action sets the position of an item to wherever the table is now. I.e. put the item in position 0, then it's current position on the susan will be calculated and saved.

### Users
Run the Users function to toggle users, i.e. make and delete users. This is the equivalent of toggle, but for people instead of items.

### Clear
This function simply clears all items from the table.

### Preset
This function allows you to use presets for items. For example, you could have a "Burger" preset that contains items such as "Chips," "Salt," and "Sauce." You could then use the preset action to activate all those items immediatley!

### Edit Presets
This function is can be used to adjust the presets.

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
- When you enable an item, the program will automatically run the "Edit" command
---
### UPDATE V1.7
- New lazy susan class
- "Cancel" command exits the action you're running
- More comments added to tests
- PEP 8 compliance maintained
---
### UPDATE V1.8
- Custom items able to be placed on table, no extra work or info required
- Try-Except-Else blocks
- Driver program deleted
- PEP 8 compliance maintained
- ---
### UPDATE V1.9
- Keeps items in a .txt file, when the program quits, items are saved.
- Infinite number of items! (Or at least however many your computer can store before crashing)
- PEP 8 compliance maintained
---
### UPDATE V2.0
- People's names
- Clear action clears all items from the table
- Automatically interprets all text in title case
- PEP 8 compliance maintained
---
### UPDATE V2.1
- Bulk toggle
- Item presets
- PEP 8 compliance maintained
---
### UPDATE V2.2
- Debugged: When no items on table, program still prints items
- FileManager class
- PEP 8 compliance maintained
---
### COMING SOON
(In order of probable appearance)
- Classes separated into different files
- Compound actions
- Clock notation
- Image emulator with Pygame