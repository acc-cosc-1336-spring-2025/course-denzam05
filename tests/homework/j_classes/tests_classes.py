#
import unittest


from src.homework.j_classes.class_a import die

class TestDie (unittest.TestCase):
    def test_roll_value_in_range (self):
        my_die = die()
        for _ in range (3):
            my_die.roll()
            value = my_die.get_rolled_value()
            self.assertIn (value, range (1, 7), f"Value {value} not in range 1 to 6")

unittest.main()

