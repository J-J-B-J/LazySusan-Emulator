import unittest  # The testing platform i'm using

import classes_and_functions.get_input as g
import main
# Include the code for the program being tested
from classes_and_functions import lazy_susan
from classes_and_functions.table_object import TableObject
from main import LazySusan
from txt_managers import item_manager
from txt_managers import preset_manager
from txt_managers import user_manager

# This variable keeps track of the printed output from the emulator, and is
# cleared in the setup
tests = []

# This is what happens in most tests:

# (1)  def test_goto_invalid_modifier(self):
# (2)      tgim_susan = emulator.LazySusan()
# (3)      sauce = emulator.TableObject("Sauce", tgim_susan)
# (4)      emulator.raw_input = 'XXXX'
# (5)      tgim_susan.goto()
# (6)      self.assertIn("You can't go to that item or modifier now.", tests)

# At 1, the test is named and defined.
# At 2, a new emulator of a lazy susan is made, and named the initials of the
# test name.
# At 3, sometimes a table object is defined, with the parent susan of above.
# At 4, the input that will be sent to the emulator is set.
# At 5, the function that is being tested is run.
# At 6, assertions are made to check that the output was expected.

rewrite = ""
while rewrite != "OK":
    rewrite = input("Are you OK to erase items, users and presets? Enter OK: ")

lazy_susan.g.test = True


class Test(unittest.TestCase):
    def setUp(self) -> None:
        tests.clear()
        self.susan = LazySusan()
        main.print = lambda output: tests.append(output)  # Send all
        # printed output from the program to the tests list
        item_manager.print = lambda output: tests.append(output)
        user_manager.print = lambda output: tests.append(output)
        preset_manager.print = lambda output: tests.append(output)
        lazy_susan.print = lambda output: tests.append(output)
        with open('txt_files/items.txt', 'w') as setup_items:
            setup_items.write("Items:\n")
        with open('txt_files/users.txt', 'w') as setup_users:
            setup_users.write("Users:\n")
        with open('txt_files/presets.txt', 'w') as setup_presets:
            setup_presets.write("Presets:\n")


class TestGetInput(Test):
    """This case tests g.get_input()"""

    def test_cancel(self):
        g.raw_input = "Cancel"
        self.assertEqual(None, g.get())

    def test_input(self):
        g.raw_input = "Hello, Get!"
        self.assertEqual(g.raw_input, g.get())


class TestInitLazySusan(Test):
    """These cases test LazySusan.__init__"""

    def test_initialize_susan_position_zero(self):
        self.assertEqual(0, self.susan.current_position)

    def test_initialize_susan_position_ninety(self):
        self.susan = LazySusan(90)
        self.assertEqual(90, self.susan.current_position)

    def test_initialize_susan_objects(self):
        self.assertDictEqual({}, self.susan.objects)


class TestListSusanItems(Test):
    """These cases test LazySusan().list_items()"""

    def test_list_no_susan_items(self):
        tests.clear()
        LazySusan.print = lambda output: tests.append(output)
        self.susan.list_items()
        self.assertListEqual(['There are no objects on the table now.'], tests)

    def test_list_susan_items(self):
        tests.clear()
        LazySusan.print = lambda output: tests.append(output)
        self.susan.objects = \
            {"Apple": TableObject("Apple", self.susan),
             "Banana": TableObject("Banana", self.susan)}
        self.susan.list_items()
        self.assertListEqual(
            ['\nItems on table:', ' - Apple', ' - Banana', '\n'], tests)


class TestSusanPrintPosition(Test):
    """These cases test LazySusan().print_current_position()"""

    def test_print_susan_position(self):
        tests.clear()
        LazySusan.print = lambda output: tests.append(output)
        self.susan.print_current_position()
        self.assertListEqual(["The table is now in position 0."], tests)


class TestTurnSusan(Test):
    """These cases test LazySusan().turn()"""

    def test_turn_float(self):
        lazy_susan.g.raw_input = float(2.5)
        self.susan.turn()
        self.assertIn("The turn you entered wasn't an integer", tests)

    def test_turn_string(self):
        lazy_susan.g.raw_input = "This is a string, not an int"
        self.susan.turn()
        self.assertIn("The turn you entered wasn't an integer", tests)

    def test_turn_45(self):
        lazy_susan.g.raw_input = int(45)
        self.susan.turn()
        self.assertIn("The table is now in position 45.", tests)

    def test_turn_45_more(self):
        self.susan = LazySusan(45)
        self.susan.print_current_position()
        lazy_susan.g.raw_input = int(45)
        self.susan.turn()
        self.assertIn("The table is now in position 90.", tests)

    def test_turn_negative_45(self):
        lazy_susan.g.raw_input = "-45"
        self.susan.turn()
        self.assertIn("The table is now in position 315.", tests)

    def test_turn_negative_45_more(self):
        self.susan = LazySusan(315)
        lazy_susan.g.raw_input = "-45"
        self.susan.turn()
        self.assertIn("The table is now in position 270.", tests)

    def test_turn_more_360(self):
        lazy_susan.g.raw_input = int(450)
        self.susan.turn()
        self.assertEqual(90, self.susan.current_position)

    def test_turn_less_negative_360(self):
        lazy_susan.g.raw_input = int(-450)
        self.susan.turn()
        self.assertEqual(270, self.susan.current_position)


class TestGotoSusan(Test):
    """These cases test LazySusan().Goto()"""

    def goto_item(self, modifier):
        with open('txt_files/users.txt', 'w') as tgi_file:
            tgi_file.write(f"Users:\n{modifier} 180")
        lazy_susan.g.raw_input = "180"
        test = self.susan.toggle()
        self.assertIn(test, self.susan.objects.values())
        self.assertEqual(0, self.susan.current_position)
        self.assertEqual(180, test.position)
        self.susan.goto()
        self.assertIn(f"The table is now in position "
                      f"{test.position - int(modifier)}.", tests)

    def test_goto_item(self):
        self.goto_item("000")

    def test_goto_item_with_modifier(self):
        self.goto_item("090")

    def test_goto_invalid_modifier(self):
        tgim_susan = LazySusan()
        lazy_susan.g.raw_input = 'XXXX'
        tgim_susan.goto()
        self.assertIn("That is not a valid user.", tests)

    def test_goto_invalid_object(self):
        with open('txt_files/users.txt', 'a') as tgio_file:
            tgio_file.write("000 A")
        tgio_susan = LazySusan()
        lazy_susan.g.raw_input = "A"
        tgio_susan.goto()
        self.assertIn("You can't go to that item or modifier now.", tests)


class TestToggleSusan(Test):
    """These cases test LazySusan().Toggle()"""

    def test_enable_and_disable(self):
        lazy_susan.g.raw_input = "180"
        sauce = self.susan.toggle()
        self.assertIn(sauce, self.susan.objects.values())
        self.assertIn("180", self.susan.objects.keys())
        self.assertEqual(180, sauce.position)
        with open('txt_files/items.txt', 'r') as te_file:
            self.assertIn("180", te_file.read())
        self.susan.toggle()
        self.assertNotIn(sauce, self.susan.objects.values())
        self.assertNotIn("180", self.susan.objects.keys())
        with open('txt_files/items.txt', 'r') as te_file:
            self.assertNotIn("0", te_file.read())


class TestEditSusan(Test):
    """These cases test LazySusan().edit()"""

    def test_edit(self):
        self.susan = LazySusan(starting_position=180)
        lazy_susan.g.raw_input = "180"
        sauce = TableObject("0", self.susan)
        sauce.used("0", self.susan)
        self.assertEqual(180, sauce.position)
        self.assertIn(sauce, self.susan.objects.values())
        self.susan.current_position = 0
        lazy_susan.g.raw_input = "0"
        self.susan.edit()
        self.assertEqual(0, self.susan.current_position)


class TestTableObject(Test):
    """These cases test TableObject()"""

    def test_init_table_object(self):
        g.raw_input = "100"
        table_object = TableObject("Object", self.susan)
        self.assertEqual("Object", table_object.name)
        self.assertEqual(100, table_object.position)
        self.assertEqual(self.susan, table_object.parent_susan)

    def test_goto_table_object(self):
        g.raw_input = "100"
        table_object = TableObject("Object", self.susan)
        table_object.goto(0)
        self.assertEqual(100, self.susan.current_position)

    def test_used_table_object(self):
        g.raw_input = "100"
        table_object = TableObject("Object", self.susan)
        table_object.used("Object")
        self.assertIn("Object", self.susan.objects.keys())
        self.assertIn(table_object, self.susan.objects.values())
        self.assertEqual(100, table_object.position)

    def test_unused_table_object(self):
        g.raw_input = "100"
        table_object = TableObject("Object", self.susan)
        table_object.used("Object")
        table_object.unused()
        self.assertNotIn("Object", self.susan.objects.keys())
        self.assertNotIn(table_object, self.susan.objects.values())


class TestItemManager(Test):
    """These cases test item_manager.py"""

    def test_clear_all(self):
        with open('txt_files/items.txt', 'w') as tca_file:
            tca_file.write("Items:\n000 A\n000 B\n000 C\n000 D\n000 E\n")
        lazy_susan.ItemManager().clear_items()
        with open('txt_files/items.txt', 'r') as tca_file:
            items = tca_file.readlines()
        self.assertListEqual([], items[1:])

    def test_recover_items(self):
        with open('txt_files/items.txt', 'w') as tri_file:
            tri_file.write("Items:\n000 Stuff\n180 More Stuff")
        item_data = lazy_susan.ItemManager().recover_items()
        self.assertListEqual([('Stuff', 0), ('More Stuff', 180)], item_data)

    def test_recover_no_items(self):
        lazy_susan.ItemManager().recover_items()
        self.assertListEqual(["No Data Found."], tests)

    def test_add_items(self):
        lazy_susan.ItemManager().add_item("Object", 100)
        lazy_susan.ItemManager().add_item("Object 2", 200)
        self.assertListEqual(['Items:\n', '100 Object\n', '200 Object 2\n'],
                             open('txt_files/items.txt').readlines())

    def test_remove_items(self):
        lazy_susan.ItemManager().add_item("Object", 100)
        lazy_susan.ItemManager().add_item("Object 2", 200)
        lazy_susan.ItemManager().remove_item("Object")
        lazy_susan.ItemManager().remove_item("Object 2")
        self.assertListEqual(['Items:\n'],
                             open('txt_files/items.txt').readlines())


class TestPresetManager(Test):
    """This case tests PresetManager().preset()"""

    def test_preset(self):
        with open('txt_files/presets.txt', 'w') as tp_file:
            tp_file.write("Presets:\n0\nA\nB\nC\n")
        lazy_susan.g.raw_input = "0"
        preset = lazy_susan.PresetManager().preset()
        self.assertListEqual([("A", 0), ("B", 0), ("C", 0)], preset)
        with open('txt_files/presets.txt', 'w') as File:
            File.write('Presets:\n')


class TestUserManager(Test):
    """These cases test UserManager()"""

    def test_read_users_file(self):
        read_data = lazy_susan.UserManager().read_users_file()
        self.assertListEqual(['Users:\n'], read_data)

    def test_get_users(self):
        with open('txt_files/users.txt', 'w') as tgu_file:
            tgu_file.write("Users:\n000 XYZ")
        output = lazy_susan.UserManager().get_users()
        self.assertDictEqual({"XYZ": "000"}, output)

    def test_edit_users(self):
        with open('txt_files/users.txt', 'w') as teu_file:
            teu_file.write("Users:\n")
        lazy_susan.g.raw_input = "0"
        lazy_susan.UserManager().edit_users()
        with open('txt_files/users.txt', 'r') as teu_file:
            users = teu_file.readlines()
        self.assertListEqual(['000 0\n'], users[1:])

    def test_get_invalid_modifier(self):
        lazy_susan.UserManager().get_modifier()
        self.assertEqual(["That is not a valid user."], tests)

    def test_get_modifier(self):
        with open('txt_files/users.txt', 'w') as teu_file:
            teu_file.write("Users:\n100 User")
        lazy_susan.g.raw_input = "User"
        modifier = lazy_susan.UserManager().get_modifier()
        self.assertEqual(100, modifier)


if __name__ == '__main__':
    unittest.main()
