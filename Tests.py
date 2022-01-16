import unittest  # The testing platform i'm using

import file_manager
import lazy_susan
import main
from main import TableObject, LazySusan  # Include the code for
# the program being tested

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

main.g.test = True


# noinspection SpellCheckingInspection
class TestEmulator(unittest.TestCase):
    """These are the tests for all modules in this program."""
    def setUp(self) -> None:
        tests.clear()
        main.print = lambda output: tests.append(output)  # Send all
        # printed output from the program to the tests list
        file_manager.print = lambda output: tests.append(output)
        lazy_susan.print = lambda output: tests.append(output)
        with open('items.txt', 'w') as setup_items:
            setup_items.write("Items:\n")
        with open('users.txt', 'w') as setup_users:
            setup_users.write("Users:\n")

    def test_goto_invalid_modifier(self):
        tgim_susan = LazySusan()
        main.g.raw_input = 'XXXX'
        tgim_susan.goto()
        self.assertIn("That is not a valid user.", tests)

    def test_goto_invalid_object(self):
        with open('users.txt', 'a') as tgio_file:
            tgio_file.write("000 A")
        tgio_susan = LazySusan()
        main.g.raw_input = "A"
        tgio_susan.goto()
        self.assertIn("You can't go to that item or modifier now.", tests)

    def test_turn_float(self):
        ttf_susan = LazySusan()
        main.g.raw_input = float(2.5)
        ttf_susan.turn()
        self.assertIn("The turn you entered wasn't an integer", tests)

    def test_turn_string(self):
        tts_susan = LazySusan()
        main.g.raw_input = "This is a string, not an int"
        tts_susan.turn()
        self.assertIn("The turn you entered wasn't an integer", tests)

    def test_turn_45(self):
        tt4_susan = LazySusan()
        main.g.raw_input = int(45)
        tt4_susan.turn()
        self.assertIn("The table is now in position 45.", tests)

    def test_turn_45_more(self):
        tt4m_susan = LazySusan(starting_position=45)
        tt4m_susan.print_current_position()
        main.g.raw_input = int(45)
        tt4m_susan.turn()
        self.assertIn("The table is now in position 90.", tests)

    def test_turn_negative_45(self):
        ttn4_susan = LazySusan()
        main.g.raw_input = "-45"
        ttn4_susan.turn()
        self.assertIn("The table is now in position 315.", tests)

    def test_turn_negative_45_more(self):
        ttn4m_susan = LazySusan(starting_position=315)
        main.g.raw_input = "-45"
        ttn4m_susan.turn()
        self.assertIn("The table is now in position 270.", tests)

    def test_turn_more_360(self):
        ttm3_susan = LazySusan()
        main.g.raw_input = int(450)
        ttm3_susan.turn()
        self.assertEqual(90, ttm3_susan.current_position)

    def test_turn_less_negative_360(self):
        # noinspection SpellCheckingInspection
        ttln3_susan = LazySusan()
        main.g.raw_input = int(-450)
        ttln3_susan.turn()
        self.assertEqual(270, ttln3_susan.current_position)

    def test_enable_and_disable(self):
        tead_susan = LazySusan()
        tead_susan.current_position = 180
        main.g.raw_input = "Sauce"
        sauce = tead_susan.toggle()
        self.assertIn(sauce, tead_susan.objects.values())
        self.assertIn("Sauce", tead_susan.objects)
        self.assertEqual(180, sauce.position)
        with open('items.txt', 'r') as te_file:
            self.assertIn("Sauce", te_file.read())
        tead_susan.toggle()
        self.assertNotIn(sauce, tead_susan.objects.values())
        self.assertNotIn("Sauce", tead_susan.objects)
        with open('items.txt', 'r') as te_file:
            self.assertNotIn("Sauce", te_file.read())

    def test_edit(self):
        ted_susan = LazySusan(starting_position=180)
        sauce = TableObject("Sauce", ted_susan)
        sauce.used("Sauce", ted_susan)
        self.assertEqual(180, sauce.position)
        self.assertIn(sauce, ted_susan.objects.values())
        ted_susan.current_position = 0
        main.g.raw_input = "Cutlery"
        ted_susan.edit()
        self.assertEqual(0, ted_susan.current_position)

    def test_toggle(self):
        tt_susan = LazySusan()
        main.g.raw_input = "Sauce"
        tt_susan.toggle()
        self.assertIn("Sauce", tt_susan.objects)

    def test_goto_item(self):
        tgi_susan = LazySusan()
        tgi_susan.current_position = 180
        with open('users.txt', 'a') as tgi_file:
            tgi_file.write("000 0")
        main.g.raw_input = "0"
        test = tgi_susan.toggle()
        tgi_susan.current_position = 0
        self.assertIn(test, tgi_susan.objects.values())
        self.assertEqual(0, tgi_susan.current_position)
        self.assertEqual(180, test.position)
        tgi_susan.goto()
        self.assertIn("The table is now in position 180.", tests)

    def test_goto_item_with_modifier(self):
        # noinspection SpellCheckingInspection
        tgiwm_susan = LazySusan()
        tgiwm_susan.current_position = 180
        with open('users.txt', 'a') as tgiwm_file:
            tgiwm_file.write("090 90")
        main.g.raw_input = "90"
        test = tgiwm_susan.toggle()
        tgiwm_susan.current_position = 0
        self.assertIn(test, tgiwm_susan.objects.values())
        self.assertEqual(0, tgiwm_susan.current_position)
        self.assertEqual(180, test.position)
        tgiwm_susan.goto()
        self.assertIn("The table is now in position 270.", tests)

    def test_cancel(self):
        main.g.raw_input = "Cancel"
        self.assertEqual(None, main.g.get("Test prompt: "))

    def test_recover_items(self):
        with open('items.txt', 'w') as tri_file:
            tri_file.write("Items:\n000 Stuff\n180 More Stuff")
        main.g.raw_input = "Yes"
        item_data = main.FileManager().recover_items()
        self.assertListEqual([('Stuff', 0), ('More Stuff', 180)], item_data)

    def test_get_users(self):
        with open('users.txt', 'w') as tgu_file:
            tgu_file.write("Users:\n000 XYZ")
        output = main.FileManager().get_users()
        self.assertDictEqual({"XYZ": "000"}, output)

    def test_edit_users(self):
        with open('users.txt', 'w') as teu_file:
            teu_file.write("Users:\n")
        main.g.raw_input = "0"
        main.FileManager().edit_users()
        with open('users.txt', 'r') as teu_file:
            users = teu_file.readlines()
        self.assertListEqual(['000 0\n'], users[1:])

    def test_clear_all(self):
        with open('items.txt', 'w') as tca_file:
            tca_file.write("Items:\n000 A\n000 B\n000 C\n000 D\n000 E\n")
        main.FileManager().clear_items()
        with open('items.txt', 'r') as tca_file:
            items = tca_file.readlines()
        self.assertListEqual([], items[1:])

    def test_preset(self):
        with open('presets.txt', 'w') as tp_file:
            tp_file.write("Presets:\n0\nA\nB\nC\n")
        main.g.raw_input = "0"
        preset = main.FileManager().preset()
        self.assertListEqual([("A", 0), ("B", 0), ("C", 0)], preset)
        with open('presets.txt', 'w') as File:
            File.write('Presets:\n')


if __name__ == '__main__':
    unittest.main()
