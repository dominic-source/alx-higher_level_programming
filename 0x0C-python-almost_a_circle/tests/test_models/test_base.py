import unittest
from models.base import Base

"""Test codes in this module"""


class TestBaseModels(unittest.TestCase):
    """Test base models"""

    def test_base_id(self):
        """Test the base class"""
        base1 = Base(30)
        base2 = Base(-1)
        base3 = Base(3)
        base4 = Base(5.73)
        self.assertEqual(base1.id, 30)
        self.assertEqual(base2.id, -1)
        self.assertEqual(base3.id, 3)
        self.assertEqual(base4.id, 5.73)

    def test_base_nb_objects(self):
        """Test the class object"""

        base10 = Base()
        base6 = Base()
        base12 = Base(3)
        base8 = Base(-1)
        base9 = Base()
        self.assertEqual(base10.id, 1)
        self.assertEqual(base6.id, 2)
        self.assertEqual(base9.id, 3)
        base11 = Base(200)
        self.assertEqual(base11.id, 200)

    def test_base_nb_objects_next(self):
        """Test the class object in other forms"""

        base1 = Base(50)
        base2 = Base(-1)
        base3 = Base(0)
        base4 = Base()
        base = Base()
        base6 = Base(2)
        base7 = Base()
        self.assertEqual(base7.id, 6)
        self.assertEqual(base6.id, 2)
        self.assertEqual(base4.id, 4)
        self.assertEqual(base.id, 5)

    def test_attr_nb_objects(self):
        """Test private class attribute"""

        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_attr_nb_objects_attr(self):
        """Test non existing attributes"""

        with self.assertRaises(AttributeError):
            print(Base.non_existing)
            print(Base.non_existing_method())


if __name__ == '__main__':
    unittest.main()
