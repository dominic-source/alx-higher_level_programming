import unittest
from models import rectangle

"""Test the rectangle model"""

class TestWidthModel(unittest.TestCase):
    """Test the rectangle models"""

    def test_width_setter_getter_1(self):
        """Test getter & setter"""

        rect1 = Rectangle(50, 23, 4, 5, 43)
        rect1.__width = 25
        self.assertEqual(rect1.__width, 25)
        self.assertEqual(rect1.id, 43)

    def test_width_setter_getter_2(self):
        """Test getter & setter"""

        rect2 = Rectangle(1000, 4)
        self.assertEqual(rect2.__width, 1000)
        self.assertEqual(rect2.id, 1)

    def test_width_setter_getter_3(self):
        """Test getter & setter"""

        rect3 = Rectangle(0, 54, 4)
        self.assertEqual(rect3.__width, 0)
        rect3.__width = 2
        self.assertEqual(rect3.__width, 2)
        self.assertEqual(rect3.id, 2)

class TestHeightModel(unittest.TestCase):
    """Test the height of the rectangle"""


    def test_width_setter_getter_1(self):
        """Test getter & setter"""

        rect1 = Rectangle(50, 23, 4, 5, 43)
        rect1.__height = 25
        self.assertEqual(rect1.__height, 25)

    def test_width_setter_getter_2(self):
        """Test getter & setter"""

        rect2 = Rectangle(4, 1000)
        self.assertEqual(rect2.__height, 1000)
        self.assertEqual(rect2.id, 3)

    def test_width_setter_getter_3(self):
        """Test getter & setter"""

        rect3 = Rectangle(0, 54, 4)
        self.assertEqual(rect3.__height, 0)
        rect3.__height = 2
        self.assertEqual(rect3.__height, 2)
        self.assertEqual(rect3.id, 4)


class TestXvalueOfModel(unittest.TestCase):
    """Test the X value of the rectangle"""


    def test_width_setter_getter_1(self):
        """Test getter & setter"""

        rect1 = Rectangle(50, 23, 4, 5, 43)
        rect1.__x = 25
        self.assertEqual(rect1.__x, 25)

    def test_width_setter_getter_2(self):
        """Test getter & setter"""

        rect2 = Rectangle(1000, 4)
        self.assertEqual(rect2.__x, 0)
        self.assertEqual(react2.id, 5)

    def test_width_setter_getter_3(self):
        """Test getter & setter"""

        rect3 = Rectangle(0, 54, 4)
        self.assertEqual(rect3.__x, 4)
        rect3.__x = 2
        self.assertEqual(rect3.__x, 2)
        self.assertEqual(rect3.id, 6)

class TestExceptionValue(unittest.TestCase):
    """Test raise Exception"""

    def test_width_setter_getter_4(self):
        """Test getter & setter"""
        
        with self.assertRaises(TypeError):
            rect4 = Rectangle()


class TestYvalueOfModel(unittest.TestCase):
    """Test the Y value of the rectangle"""


    def test_width_setter_getter_1(self):
        """Test getter & setter"""

        rect1 = Rectangle(50, 23, 4, 5, 43)
        rect1.__y = 25
        self.assertEqual(rect1.__y, 25)
        self.assertEqual(rect1.id, 43)

    def test_width_setter_getter_2(self):
        """Test getter & setter"""

        rect2 = Rectangle(1000, 4)
        self.assertEqual(rect2.__y, 0)
        self.assertEqual(rect2.id, 7)

    def test_width_setter_getter_3(self):
        """Test getter & setter"""

        rect3 = Rectangle(0, 54, 4, 32, 19)
        self.assertEqual(rect3.__y, 32)
        rect3.__y = 2
        self.assertEqual(rect3.__y, 2)
        self.assertEqual(rect3.id, 19)


if __name__ == '__main__':
    unittest.main()
