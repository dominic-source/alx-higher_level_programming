import unittest
from models.rectangle import Rectangle

"""Test the rectangle model"""


class TestAWidthModel(unittest.TestCase):
    """Test the rectangle models"""

    def setUp(self):
        """setup things"""

        self.rect1 = Rectangle(50, 23, 4, 5, 43)
        self.rect2 = Rectangle(1000, 4)
        self.rect3 = Rectangle(0, 54, 4)

    def tearDown(self):
        """delete rectangle"""

        del self.rect1
        del self.rect2
        del self.rect3

    def test_width_setter_getter_1(self):
        """Test getter & setter"""

        self.rect1.width = 25
        self.assertEqual(self.rect1.width, 25)
        self.assertEqual(self.rect1.id, 43)

    def test_width_setter_getter_2(self):
        """Test getter & setter"""

        self.assertEqual(self.rect2.width, 1000)

    def test_width_setter_getter_3(self):
        """Test getter & setter"""

        self.assertEqual(self.rect3.width, 0)
        self.rect3.width = 2
        self.assertEqual(self.rect3.width, 2)


class TestBHeightModel(unittest.TestCase):
    """Test the height of the rectangle"""

    def setUp(self):
        """setup things"""

        self.rect4 = Rectangle(50, 23, 4, 5, 43)
        self.rect5 = Rectangle(4, 1000)
        self.rect6 = Rectangle(0, 54, 4)

    def tearDown(self):
        """delete rectangle"""

        del self.rect4
        del self.rect5
        del self.rect6

    def test_width_setter_getter_4(self):
        """Test getter & setter"""

        self.rect4.height = 25
        self.assertEqual(self.rect4.height, 25)

    def test_width_setter_getter_5(self):
        """Test getter & setter"""

        self.assertEqual(self.rect5.height, 1000)

    def test_width_setter_getter_6(self):
        """Test getter & setter"""

        self.assertEqual(self.rect6.height, 54)
        self.rect6.height = 2
        self.assertEqual(self.rect6.height, 2)


class TestCXvalueOfModel(unittest.TestCase):
    """Test the X value of the rectangle"""

    def setUp(self):
        """setup things"""

        self.rect7 = Rectangle(50, 23, 4, 5, 43)
        self.rect8 = Rectangle(1000, 4)
        self.rect9 = Rectangle(0, 54, 4)

    def tearDown(self):
        """delete rectangle"""

        del self.rect7
        del self.rect8
        del self.rect9

    def test_width_setter_getter_7(self):
        """Test getter & setter"""

        self.rect7.x = 25
        self.assertEqual(self.rect7.x, 25)

    def test_width_setter_getter_8(self):
        """Test getter & setter"""

        self.assertEqual(self.rect8.x, 0)

    def test_width_setter_getter_9(self):
        """Test getter & setter"""

        self.assertEqual(self.rect9.x, 4)
        self.rect9.x = 2
        self.assertEqual(self.rect9.x, 2)


class TestDExceptionValue(unittest.TestCase):
    """Test raise Exception"""

    def test_width_setter_getter_10(self):
        """Test getter & setter"""

        with self.assertRaises(TypeError):
            self.rect10 = Rectangle()


class TestEYvalueOfModel(unittest.TestCase):
    """Test the Y value of the rectangle"""

    def setUp(self):
        """setup things"""

        self.rect11 = Rectangle(50, 23, 4, 5, 43)
        self.rect12 = Rectangle(1000, 4)
        self.rect13 = Rectangle(0, 54, 4, 32, 19)

    def tearDown(self):
        """delete rectangle"""

        del self.rect11
        del self.rect12
        del self.rect13

    def test_width_setter_getter_11(self):
        """Test getter & setter"""

        self.rect11.y = 25
        self.assertEqual(self.rect11.y, 25)
        self.assertEqual(self.rect11.id, 43)

    def test_width_setter_getter_12(self):
        """Test getter & setter"""

        self.assertEqual(self.rect12.y, 0)

    def test_width_setter_getter_13(self):
        """Test getter & setter"""

        self.assertEqual(self.rect13.y, 32)
        self.rect13.y = 2
        self.assertEqual(self.rect13.y, 2)
        self.assertEqual(self.rect13.id, 19)


if __name__ == '__main__':
    suite_loader = unittest.TestLoader()
    suite1 = suite_loader.loadTestsFromTestCase(TestAWidthModel)
    suite2 = suite_loader.loadTestsFromTestCase(TestBHeightModel)
    suite3 = suite_loader.loadTestsFromTestCase(TestCXvalueOfModel)
    suite4 = suite_loader.loadTestsFromTestCase(TestDExceptionValue)
    suite5 = suite_loader.loadTestsFromTestCase(TestEYvalueOfModel)
    suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5])
    unittest.TestRunner(verbosity=2).run(suite)
