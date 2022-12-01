import unittest
from calc import div


class TestCalc(unittest.TestCase):

    def test_div(self):
        self.assertEqual(4, div(8, 2))
        self.assertEqual(3, div(6, 2))
        with self.assertRaises(ValueError):
            div(8, 0)