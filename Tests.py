import unittest  # The testing platform i'm using
import \
    lazy_suzan_emulator as emulator  # Include the code for the program

# being tested

# This variable keeps track of the printed output from the emulator, and is
# cleared in the setup
tests = []

# This is what happens in most tests:

# (1)  def test_goto_invalid_modifier(self):
# (2)      tgim_susan = emulator.LazySusan()
# (3)      sauce = emulator.TableObject("Sauce", tgim_susan)
# (4)      emulator.raw_input = lambda _: 'XXXX'
# (5)      tgim_susan.goto()
# (6)      self.assertIn("You can't go to that item or modifier now.", tests)

# At 1, the test is named and defined.
# At 2, a new emulator of a lazy susan is made, and named the initials of the
# test name.
# At 3, sometimes a table object is defined, with the parent susan of above.
# At 4, the input that will be sent to the emulator is set.
# At 5, the function that is being tested is run.
# At 6, assertions are made to check that the output was expected.


class TestEmulator(unittest.TestCase):
    def setUp(self) -> None:
        tests.clear()
        emulator.print = lambda output: tests.append(output)  # Send all
        # printed output from emulator to the tests list

    def test_goto_invalid_modifier(self):
        tgim_susan = emulator.LazySusan()
        emulator.raw_input = lambda _: 'XXXX'
        tgim_susan.goto()
        self.assertIn("You can't go to that item or modifier now.", tests)

    def test_goto_invalid_object(self):
        tgio_susan = emulator.LazySusan()
        emulator.raw_input = lambda _: 0
        tgio_susan.goto()
        self.assertIn("You can't go to that item or modifier now.", tests)

    def test_toggle_too_many_items(self):
        tttmi_susan = emulator.LazySusan()
        items_to_toggle = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                           "K"]
        for letter in items_to_toggle:
            emulator.raw_input = lambda _: letter
            tttmi_susan.toggle()
        self.assertIn("Sorry, but you can only have 10 items on the table.",
                      tests)

    def test_edit_invalid_object(self):
        teio_susan = emulator.LazySusan()
        emulator.raw_input = lambda _: 'XXXX'
        teio_susan.edit()
        self.assertIn("The item you asked for doesn't exist.", tests)

    def test_turn_float(self):
        ttf_susan = emulator.LazySusan()
        emulator.raw_input = lambda _: float(2.5)
        ttf_susan.turn()
        self.assertIn("The turn you entered wasn't an integer", tests)

    def test_turn_string(self):
        tts_susan = emulator.LazySusan()
        emulator.raw_input = lambda _: "This is a string, not an int"
        tts_susan.turn()
        self.assertIn("The turn you entered wasn't an integer", tests)

    def test_turn_45(self):
        tt4_susan = emulator.LazySusan()
        emulator.raw_input = int(45)
        tt4_susan.turn()
        self.assertIn("The table is now in position 45.", tests)

    def test_turn_45_more(self):
        tt4m_susan = emulator.LazySusan(starting_position=45)
        tt4m_susan.print_current_position()
        emulator.raw_input = int(45)
        tt4m_susan.turn()
        self.assertIn("The table is now in position 90.", tests)

    def test_turn_negative_45(self):
        ttn4_susan = emulator.LazySusan()
        emulator.raw_input = "-45"
        ttn4_susan.turn()
        self.assertIn("The table is now in position 315.", tests)

    def test_turn_negative_45_more(self):
        ttn4m_susan = emulator.LazySusan(starting_position=315)
        emulator.raw_input = "-45"
        ttn4m_susan.turn()
        self.assertIn("The table is now in position 270.", tests)

    def test_turn_more_360(self):
        ttm3_susan = emulator.LazySusan()
        emulator.raw_input = int(450)
        ttm3_susan.turn()
        self.assertEqual(90, ttm3_susan.current_position)

    def test_turn_more_negative_360(self):
        ttmn3_susan = emulator.LazySusan()
        emulator.raw_input = int(-450)
        ttmn3_susan.turn()
        self.assertEqual(270, ttmn3_susan.current_position)

    def test_enable(self):
        te_susan = emulator.LazySusan()
        sauce = emulator.TableObject("Sauce", te_susan)
        sauce.position = 0
        te_susan.current_position = 180
        emulator.raw_input = "Sauce"
        te_susan.toggle()
        self.assertEqual(True, sauce.use)
        self.assertIn("Sauce", te_susan.objects)
        self.assertEqual(180, sauce.position)

    def test_disable(self):
        td_susan = emulator.LazySusan()
        sauce = emulator.TableObject("Sauce", td_susan)
        emulator.raw_input = "Sauce"
        td_susan.toggle()
        td_susan.toggle()
        self.assertEqual(False, sauce.use)
        self.assertNotIn("Sauce", td_susan.objects)

    def test_edit(self):
        ted_susan = emulator.LazySusan(starting_position=180)
        sauce = emulator.TableObject("Sauce", ted_susan)
        sauce.used()
        self.assertEqual(180, sauce.position)
        self.assertEqual(True, sauce.use)
        ted_susan.current_position = 0
        emulator.raw_input = "Cutlery"
        ted_susan.edit()
        self.assertEqual(0, ted_susan.current_position)

    def test_edit_when_disabled(self):
        tewd_susan = emulator.LazySusan()
        sauce = emulator.TableObject("Sauce", tewd_susan)
        tewd_susan.current_position = 180
        sauce.position = 0
        self.assertEqual(False, sauce.use)
        self.assertEqual(180, tewd_susan.current_position)
        self.assertEqual(0, sauce.position)
        emulator.raw_input = "Sauce"
        tewd_susan.toggle()
        self.assertEqual(True, sauce.use)
        self.assertEqual(180, tewd_susan.current_position)
        self.assertEqual(180, sauce.position)

    def test_goto_item(self):
        tgi_susan = emulator.LazySusan()
        test = emulator.TableObject("0", tgi_susan)
        tgi_susan.current_position = 180
        emulator.raw_input = "0"
        tgi_susan.toggle()
        tgi_susan.current_position = 0
        self.assertEqual(True, test.use)
        self.assertEqual(0, tgi_susan.current_position)
        self.assertEqual(180, test.position)
        tgi_susan.goto()
        self.assertIn("The table is now in position 180.", tests)

    def test_goto_item_with_modifier(self):
        tgiwm_susan = emulator.LazySusan()
        test = emulator.TableObject("90", tgiwm_susan)
        tgiwm_susan.current_position = 180
        emulator.raw_input = "90"
        tgiwm_susan.toggle()
        tgiwm_susan.current_position = 0
        self.assertEqual(True, test.use)
        self.assertEqual(0, tgiwm_susan.current_position)
        self.assertEqual(180, test.position)
        tgiwm_susan.goto()
        self.assertIn("The table is now in position 270.", tests)

    def test_cancel(self):
        emulator.raw_input = "Cancel"
        self.assertEqual(None, emulator.get_input())


if __name__ == '__main__':
    unittest.main()
