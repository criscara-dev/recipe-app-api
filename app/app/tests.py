"""
Sample tests for the app.
"""

from django.test import SimpleTestCase
from . import calc


# create class for testing
class CalcTests(SimpleTestCase):
    """test the calc module"""

    def test_add_numbers(self):
        """test that 5 + 6 = 11"""
        self.assertEqual(calc.add(5, 6), 11)

    def test_subtract_numbers(self):
        """test that 5 - 6 = -1"""
        self.assertEqual(calc.subtract(5, 6), -1)
