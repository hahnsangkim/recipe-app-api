from django.test import TestCase

from app.calc import add
from app.calc import subtract

class CalcTests (TestCase):

    def test_calc(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(2, 8), 10)

    def test_subt(self):
        """Test that values are substracted and returned"""
        self.assertEqual(subtract(5, 11), 6)