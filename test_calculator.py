import unittest
from calculator import add_numbers

class TestCalculator(unittest.TestCase):
    def test_add_success(self):
        # This should pass because 2 + 3 = 5
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_fail_check(self):
        # This ensures our calculator doesn't return wrong answers
        self.assertNotEqual(add_numbers(2, 2), 5)

if __name__ == '__main__':
    unittest.main()