import unittest  # The testing platform i'm using

import classes_and_functions.class_text as class_text
import classes_and_functions.class_emulator as e
import classes_and_functions.class_lazy_susan as ls
import classes_and_functions.func_get_input as g
import txt_managers.manager_users as u
import txt_managers.manager_presets as p

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

g.test = True


# noinspection SpellCheckingInspection
class TestEmulator(unittest.TestCase):
    """These are the tests for all modules in this program."""

    def setUp(self) -> None:
        tests.clear()
        class_text.print = lambda output: tests.append(output)  # Send all
        # printed output from the program to the tests list

        with open('txt_files/saved_items.txt', 'w') as setup_items:
            setup_items.write("Items:\n")
        with open('txt_files/saved_users.txt', 'w') as setup_users:
            setup_users.write("Users:\n")

    def test_goto_invalid_modifier(self):
        g.raw_input = 'XXXX'
        self.assertIsNone(
            u.UserManager(e.Emulator()).get_modifier(e.Emulator()))

    def test_goto_invalid_object(self):
        with open('txt_files/saved_users.txt', 'a') as tgio_file:
            tgio_file.write("180 A")
        tgio_susan = ls.LazySusan(e.Emulator())
        g.raw_input = "A"
        tgio_susan.goto(tgio_susan)
        self.assertEqual(0, tgio_susan.current_position)

    def test_turn_float(self):
        ttf_susan = ls.LazySusan(e.Emulator())
        g.raw_input = float(2.5)
        ttf_susan.turn(ttf_susan)
        self.assertEqual(0, ttf_susan.current_position)

    def test_turn_string(self):
        tts_susan = ls.LazySusan(e.Emulator())
        g.raw_input = "This is a string, not an int"
        tts_susan.turn(tts_susan)
        self.assertEqual(0, tts_susan.current_position)

    def test_turn_45(self):
        tt4_susan = ls.LazySusan(e.Emulator())
        g.raw_input = int(45)
        tt4_susan.turn(tt4_susan)
        self.assertEqual(45, tt4_susan.current_position)

    def test_turn_45_more(self):
        tt4m_susan = ls.LazySusan(e.Emulator(), starting_position=45)
        tt4m_susan.print_current_position()
        g.raw_input = int(45)
        tt4m_susan.turn(tt4m_susan)
        self.assertEqual(90, tt4m_susan.current_position)

    def test_turn_negative_45(self):
        ttn4_susan = ls.LazySusan(e.Emulator())
        g.raw_input = "-45"
        ttn4_susan.turn(ttn4_susan)
        self.assertEqual(315, ttn4_susan.current_position)

    def test_turn_negative_45_more(self):
        ttn4m_susan = ls.LazySusan(e.Emulator(), starting_position=315)
        g.raw_input = "-45"
        ttn4m_susan.turn(ttn4m_susan)
        self.assertEqual(270, ttn4m_susan.current_position)

    def test_turn_more_360(self):
        ttm3_susan = ls.LazySusan(e.Emulator())
        g.raw_input = int(450)
        ttm3_susan.turn(ttm3_susan)
        self.assertEqual(90, ttm3_susan.current_position)

    def test_turn_less_negative_360(self):
        # noinspection SpellCheckingInspection
        ttln3_susan = ls.LazySusan(e.Emulator())
        g.raw_input = int(-450)
        ttln3_susan.turn(ttln3_susan)
        self.assertEqual(270, ttln3_susan.current_position)

    def test_enable_and_disable(self):
        tead_susan = ls.LazySusan(e.Emulator())
        tead_susan.current_position = 180
        g.raw_input = "Sauce"
        sauce = tead_susan.toggle(tead_susan)
        self.assertIn(sauce, tead_susan.objects.values())
        self.assertIn("Sauce", tead_susan.objects)
        self.assertEqual(180, sauce.position)
        with open('txt_files/saved_items.txt', 'r') as te_file:
            self.assertIn("Sauce", te_file.read())
        tead_susan.toggle(tead_susan)
        self.assertNotIn(sauce, tead_susan.objects.values())
        self.assertNotIn("Sauce", tead_susan.objects)
        with open('txt_files/saved_items.txt', 'r') as te_file:
            self.assertNotIn("Sauce", te_file.read())

    def test_edit(self):
        ted_emulaltor = e.Emulator()
        ted_susan = ls.LazySusan(ted_emulaltor, starting_position=180)
        sauce = ls.TableObject("Sauce", ted_susan, ted_emulaltor)
        sauce.used("Sauce", ted_susan)
        self.assertEqual(180, sauce.position)
        self.assertIn(sauce, ted_susan.objects.values())
        ted_susan.current_position = 0
        g.raw_input = "Cutlery"
        ted_susan.edit(ted_susan)
        self.assertEqual(0, ted_susan.current_position)

    def test_toggle(self):
        tt_susan = ls.LazySusan(e.Emulator())
        g.raw_input = "Sauce"
        tt_susan.toggle(tt_susan)
        self.assertIn("Sauce", tt_susan.objects)

    def test_goto_item(self):
        tgi_susan = ls.LazySusan(e.Emulator())
        tgi_susan.current_position = 180
        with open('txt_files/saved_users.txt', 'a') as tgi_file:
            tgi_file.write("000 0")
        g.raw_input = "0"
        test = tgi_susan.toggle(tgi_susan)
        tgi_susan.current_position = 0
        self.assertIn(test, tgi_susan.objects.values())
        self.assertEqual(0, tgi_susan.current_position)
        self.assertEqual(180, test.position)
        tgi_susan.goto(e.Emulator())
        self.assertEqual(180, tgi_susan.current_position)

    def test_goto_item_with_modifier(self):
        # noinspection SpellCheckingInspection
        tgiwm_susan = ls.LazySusan(e.Emulator())
        tgiwm_susan.current_position = 180
        with open('txt_files/saved_users.txt', 'a') as tgiwm_file:
            tgiwm_file.write("090 90")
        g.raw_input = "90"
        test = tgiwm_susan.toggle(tgiwm_susan)
        tgiwm_susan.current_position = 0
        self.assertIn(test, tgiwm_susan.objects.values())
        self.assertEqual(0, tgiwm_susan.current_position)
        self.assertEqual(180, test.position)
        tgiwm_susan.goto(tgiwm_susan)
        self.assertEqual(270, tgiwm_susan.current_position)

    def test_cancel(self):
        tc_susan = ls.LazySusan
        g.raw_input = "Cancel"
        self.assertEqual(None, g.get("Test prompt: ", tc_susan))

    def test_recover_items(self):
        with open('txt_files/saved_items.txt', 'w') as tri_file:
            tri_file.write("Items:\n000 Stuff\n180 More Stuff")
        g.raw_input = "Yes"
        item_data = e.ItemManager(e.Emulator()).recover_items()
        self.assertListEqual([('Stuff', 0), ('More Stuff', 180)], item_data)

    def test_get_users(self):
        with open('txt_files/saved_users.txt', 'w') as tgu_file:
            tgu_file.write("Users:\n000 XYZ")
        output = u.UserManager(e.Emulator()).get_users()
        self.assertDictEqual({"XYZ": "000"}, output)

    def test_edit_users(self):
        teu_susan = ls.LazySusan(e.Emulator())
        with open('txt_files/saved_users.txt', 'w') as teu_file:
            teu_file.write("Users:\n")
        g.raw_input = "0"
        u.UserManager(e.Emulator()).edit_users(teu_susan)
        with open('txt_files/saved_users.txt', 'r') as teu_file:
            users = teu_file.readlines()
        self.assertListEqual(['000 0\n'], users[1:])

    def test_clear_all(self):
        with open('txt_files/saved_items.txt', 'w') as tca_file:
            tca_file.write("Items:\n000 A\n000 B\n000 C\n000 D\n000 E\n")
        e.ItemManager(e.Emulator()).clear_items()
        with open('txt_files/saved_items.txt', 'r') as tca_file:
            items = tca_file.readlines()
        self.assertListEqual([], items[1:])

    def test_preset(self):
        with open('txt_files/saved_presets.txt', 'w') as tp_file:
            tp_file.write("Presets:\n0\nA\nB\nC\n")
        g.raw_input = "0"
        tp_emulator = e.Emulator()
        preset = p.PresetManager().preset(tp_emulator)
        self.assertListEqual([("A", 0), ("B", 0), ("C", 0)], preset)
        with open('txt_files/saved_presets.txt', 'w') as File:
            File.write('Presets:\n')


if __name__ == '__main__':
    unittest.main()
