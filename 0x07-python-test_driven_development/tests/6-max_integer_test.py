#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):

        """Test the maximum integers in a list of integers"""

        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5, 0, 99, 3, 87, 120, 0]), 120)
        self.assertEqual(max_integer([-1, -10]), -1)
        self.assertEqual(max_integer([-1, 0]), 0)
        self.assertEqual(max_integer([0, 0, -1, 1]), 1)
        self.assertEqual(max_integer([0, -1]), 0)
        self.assertEqual(max_integere([40], 40))
        with self.assertRaises(TypeError):
            print(max_integer(['5', 0, 99, 3, 87, [120], '0']))
        with self.assertRaises(TypeError):
            print(max_integer([5, None, 99, 3, 87, 120, 0]))
        with self.assertRaises(NameError):
            print(max_integer([5, j, 99, 3, 87, 120, 0]))
        self.assertEqual(max_integer([150, 0, 99, 3, 87, 120, 0]), 150)
        with self.assertRaises(TypeError):
            max_integer([[8], 0, 99, 3, 87, 120, 0])


if __name__ == '__main__':
    unittest.main()
