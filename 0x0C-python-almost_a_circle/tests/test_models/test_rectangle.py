import unittest
from models.rectangle import Rectangle
from models.base import Base

"""Test the rectangle model"""


class TestAWidthModel(unittest.TestCase):
    """Test the rectangle models"""

    def setUp(self):
        """setup things"""

        self.rect1 = Rectangle(50, 23, 4, 5, 43)
        self.rect2 = Rectangle(1000, 4)
        self.rect3 = Rectangle(8, 54, 4)

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

        self.assertEqual(self.rect3.width, 8)
        self.rect3.width = 2
        self.assertEqual(self.rect3.width, 2)


class TestBHeightModel(unittest.TestCase):
    """Test the height of the rectangle"""

    def setUp(self):
        """setup things"""

        self.rect4 = Rectangle(50, 23, 4, 5, 43)
        self.rect5 = Rectangle(4, 1000)
        self.rect6 = Rectangle(8, 54, 4)

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
        self.rect9 = Rectangle(8, 54, 4)

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

    def setUp(self):
        """Setup somethings"""

        self.width = Rectangle(3, 4, 5, 7)
        self.height = Rectangle(3, 4, 5, 7)
        self.x = Rectangle(3, 4, 5, 7)
        self.y = Rectangle(3, 4, 5, 7)

    def test_Awidth_setter_getter_10(self):
        """Test getter & setter"""

        with self.assertRaises(TypeError):
            self.rect10 = Rectangle()

    def test_Bwidth_height_x_y_dict(self):
        """Test setter dict"""

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            width = Rectangle({"tera": 5}, 4, 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.width.width = {"tera": 5}
        
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            height = Rectangle(4, {"dfd": 5}, 54)

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            self.height.height = {"tera": 8}

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            x = Rectangle(4, 4, {"dfd": 5}, 54)

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.x.x = {"tera": 8}

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            y = Rectangle(4, 7, 8, {"dfd": 5}, 54)
        
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.y.y = {"tera": 8}

    def test_Cwidth_height_x_y_list(self):
        """Test setter list"""

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            width = Rectangle([4, 5], 4, 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
           self.width.width = [4, 5]

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            self.height = Rectangle(4, ["dfd", 5], 54)

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            self.height.height = [4, 5]

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            x = Rectangle(4, 4, ["dfd", 5], 54)

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.x.x = [4, 6]

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            y = Rectangle(4, 7, 8, ["dfd", 5], 54)

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.y.y = [3, 9]

    def test_Dwidth_height_x_y_str(self):
        """Test setter str"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            width = Rectangle("tera", 4, 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.width.width = 'sf'
        
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            height = Rectangle(4, "dfd", 54)

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            self.height.height = "fa"

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            x = Rectangle(4, 4, "dfd", 54)

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.x.x = "faw"

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            y = Rectangle(4, 7, 8, "dfd", 54)

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.y.y = "faf"

    def test_Ewidth_height_x_y_None(self):
        """Test setter None"""
       
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            width = Rectangle(None, 4, 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.width.width = None

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            height = Rectangle(4, None, 54)

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            self.height.height = None

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            x = Rectangle(4, 4, None, 54)

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.x.x = None

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            y = Rectangle(4, 7, 8, None, 54)

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.y.y = None

    def test_Fwidth_height_x_y_turple(self):
        """Test setter turple"""
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            width = Rectangle(("tera", 5), 4, 5)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.width.width = ("tera",5)
        
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            height = Rectangle(4, ("dfd", 5), 54)

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            self.height.height = ("dfa", 4)

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            x = Rectangle(4, 4, ("dfd", 5), 54)

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.x.x = ("faf", 4)

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            y = Rectangle(4, 7, 8, ("dfd", 5), 54)

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.y.y = ("fa", 3)

    def test_Hwidth_height_x_y_empty(self):
        """Test setter empty"""

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            height = Rectangle(4)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            width = Rectangle()

    def test_Gwidth_height_x_y_zero(self):
        """Test width height x y value"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            width = Rectangle(-1, 5, 6)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            width2 = Rectangle(0, 3, 9)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            width3 = Rectangle(-244, 4, 0)
        
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            height = Rectangle(90, -1, 45)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            height2 = Rectangle(23, -234, 43)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            height3 = Rectangle(34, 0, 23)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            x = Rectangle(32, 53, -1, 43)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            x2 = Rectangle(32, 5, -245, 9)
        
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            y = Rectangle(5, 2, 43, -5)
        
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            y2 = Rectangle(33, 5, 90, -1)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            y3 = Rectangle(32, 43, 2, -3433)



class TestEYvalueOfModel(unittest.TestCase):
    """Test the Y value of the rectangle"""

    def setUp(self):
        """setup things"""

        self.rect11 = Rectangle(50, 23, 4, 5, 43)
        self.rect12 = Rectangle(1000, 4)
        self.rect13 = Rectangle(5, 54, 4, 32, 19)

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


class TestFArea(unittest.TestCase):
    """Test the area of the rectangle"""
    
    def setUp(self):
        """set up the test"""

        self.ar = Rectangle(4, 2, 9, 34)
        self.ar2 = Rectangle(1, 1000, 4, 56)
        self.ar3 = Rectangle(1245, 144, 0, 2)

    def tearDown(self):
        """Destroy the instances of the class"""

        del self.ar
        del self.ar2
        del self.ar3
    
    def test_Aarea(self):
        """Test the area of the rectangle"""

        self.assertEqual(self.ar.area(), 8)
        self.assertEqual(self.ar2.area(), 1000)
        self.assertEqual(self.ar3.area(), 179280)

class TestGInheritance(unittest.TestCase):
    """Test for inheritance"""

    def test_inherit(self):
        """Test inheritance"""

        self.assertTrue(issubclass(Rectangle, Base))
    
    def test_instance(self):
        """Test instance"""

        rect = Rectangle(4, 5, 6)
        self.assertTrue(isinstance(rect, Rectangle))
        self.assertTrue(isinstance(rect, Base))

class TestHDisplay(unittest.TestCase):
    """Test the display method"""

    def setUp(self):
        """Set up the display testing"""

        self.dis = Rectangle(1, 1)
        self.dis2 = Rectangle(2, 2)
        self.dis3 = Rectangle(5, 5)
        self.dis4 = Rectangle(10, 10)
        self.dis5 = Rectangle(2, 7)

    def tearDown(self):
        """Tear down the display testing"""

        del self.dis
        del self.dis2
        del self.dis3
        del self.dis4
        del self.dis5

    def test_display(self):
        """Test the display method"""

        string = '##########\n##########\n##########\n##########\n##########\n'
        string += '##########\n##########\n##########\n##########\n##########\n'

        self.assertEqual(self.dis.display(), '#\n')
        self.assertEqual(self.dis2.dispaly(), '##\n##\n')
        self.assertEqual(self.dis3.display(), '#####\n#####\n#####\n#####\n#####\n')
        self.assertEqual(self.dis4.display(), string)
        self.assertEqual(self.dis5.display(), '##\n##\n##\n##\n##\n##\n')


if __name__ == '__main__':
    
    suite_loader = unittest.TestLoader()

    suite1 = suite_loader.loadTestsFromTestCase(TestAWidthModel)
    suite2 = suite_loader.loadTestsFromTestCase(TestBHeightModel)
    suite3 = suite_loader.loadTestsFromTestCase(TestCXvalueOfModel)
    suite4 = suite_loader.loadTestsFromTestCase(TestDExceptionValue)
    suite5 = suite_loader.loadTestsFromTestCase(TestEYvalueOfModel)
    suite6 = suite_loader.loadTestsFromTestCase(TestFArea)
    suite7 = suite_loader.loadTestsFromTestCase(TestGInheritance)

    suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5, suite6, suite7])
    unittest.TestRunner(verbosity=2).run(suite)
