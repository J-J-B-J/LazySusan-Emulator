import unittest
import lazy_suzan_emulator as emulator


# This function replaces the print() function
# It prints what the print() function was going to print, then adds the text to the test array
tests = []


class TestEmulator(unittest.TestCase):
    def setUp(self) -> None:
        tests.clear()
        emulator.print = lambda output: tests.append(output)

    def test_invalid_action(self):
        emulator.raw_input = lambda _: 'XXXX'
        emulator.main()
        self.assertIn("The action you entered wasn't valid", tests)

    def test_goto_invalid_modifier(self):
        emulator.raw_input = lambda _: 'XXXX'
        emulator.goto()
        self.assertIn("You can't go to that item or modifier now.", tests)

    def test_goto_invalid_object(self):
        emulator.raw_input = lambda _: 0
        emulator.goto()
        self.assertIn("You can't go to that item or modifier now.", tests)

    def test_toggle_invalid_object(self):
        emulator.raw_input = lambda _: 'XXXX'
        emulator.toggle()
        self.assertIn("The item you asked for doesn't exist.", tests)

    def test_edit_invalid_object(self):
        emulator.raw_input = lambda _: 'XXXX'
        emulator.edit()
        self.assertIn("The item you asked for doesn't exist.", tests)

    def test_turn_float(self):
        emulator.raw_input = lambda _: float(2.5)
        emulator.turn()
        self.assertIn("The turn you entered wasn't an integer", tests)

    def test_turn_string(self):
        emulator.raw_input = lambda _: "This is a string, not an int"
        emulator.turn()
        self.assertIn("The turn you entered wasn't an integer", tests)

    def test_turn_45(self):
        emulator.current_position = 0
        emulator.raw_input = int(45)
        emulator.turn()
        self.assertEqual(45, emulator.current_position)
        emulator.turn()
        self.assertEqual(90, emulator.current_position)

    def test_turn_negative_45(self):
        emulator.raw_input = int(-45)
        emulator.turn()
        self.assertEqual(45, emulator.current_position)
        emulator.turn()
        self.assertEqual(0, emulator.current_position)

    def test_enable(self):
        emulator.cutlery.use = False
        emulator.cutlery.position = 0
        emulator.current_position = 180
        emulator.raw_input = "Cutlery"
        emulator.toggle()
        self.assertEqual(True, emulator.cutlery.use)
        self.assertIn("Cutlery", emulator.objects)
        self.assertEqual(180, emulator.cutlery.position)

    def test_disable(self):
        emulator.cutlery.used()
        emulator.raw_input = "Cutlery"
        emulator.toggle()
        self.assertEqual(False, emulator.cutlery.use)
        self.assertNotIn("Cutlery", emulator.objects)

    def test_edit(self):
        emulator.current_position = 180
        emulator.cutlery.used()
        self.assertEqual(180, emulator.cutlery.position)
        self.assertEqual(True, emulator.cutlery.use)
        emulator.current_position = 0
        emulator.raw_input = "Cutlery"
        emulator.edit()
        self.assertEqual(0, emulator.cutlery.position)

    def test_edit_when_disabled(self):
        emulator.current_position = 180
        emulator.cutlery.unused()
        emulator.cutlery.position = 0
        self.assertEqual(False, emulator.cutlery.use)
        self.assertEqual(180, emulator.current_position)
        self.assertEqual(0, emulator.cutlery.position)
        emulator.raw_input = "Cutlery"
        emulator.toggle()
        self.assertEqual(True, emulator.cutlery.use)
        self.assertEqual(180, emulator.current_position)
        self.assertEqual(180, emulator.cutlery.position)

    def test_goto_item(self):
        test = emulator.TableObject("0")
        emulator.current_position = 180
        test.used()
        emulator.current_position = 0
        self.assertEqual(True, test.use)
        self.assertEqual(0, emulator.current_position)
        self.assertEqual(180, test.position)
        emulator.raw_input = "0"
        emulator.goto()
        print(tests)
        self.assertEqual(180, emulator.current_position)

    def test_goto_item_with_modifier(self):
        test = emulator.TableObject("90")
        emulator.current_position = 180
        test.used()
        emulator.current_position = 0
        self.assertEqual(True, test.use)
        self.assertEqual(0, emulator.current_position)
        self.assertEqual(180, test.position)
        emulator.raw_input = "90"
        emulator.goto()
        print(tests)
        self.assertEqual(270, emulator.current_position)


if __name__ == '__main__':
    unittest.main()
