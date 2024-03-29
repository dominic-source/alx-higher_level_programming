import unittest
from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
import sys

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

        self.dis1 = Rectangle(1, 1)
        self.dis3 = Rectangle(5, 5)
        self.dis4 = Rectangle(10, 10)
        self.dis5 = Rectangle(2, 7)

        self.dis2 = Rectangle(4, 8, 32, 54, 9)
        self.dis6 = Rectangle(1, 1, 1, 1, 1)
        
        self.dis7 = Rectangle(3, 5, 2, 1)
        self.dis8 = Rectangle(4, 4, 1, 0)
        self.dis9 = Rectangle(5, 3, 0, 4)

    def tearDown(self):
        """Tear down the display testing"""

        del self.dis1
        del self.dis3
        del self.dis4
        del self.dis5
        del self.dis2
        del self.dis6
        del self.dis7
        del self.dis8
        del self.dis9

    def test_display(self):
        """Test the display method"""

        string = '##########\n##########\n##########\n##########\n##########\n'
        string += '##########\n##########\n##########\n##########\n##########'

        capture_output = StringIO()
        sys.stdout = capture_output
        self.dis4.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value.strip(), string)

    def test_Bdisplay(self):
        """Test the display part B"""
        
        capture_output = StringIO()
        sys.stdout = capture_output
        self.dis1.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value.strip(), '#')

    def test_Cdisplay(self):
        """Test the display part C"""
        
        capture_output = StringIO()
        sys.stdout = capture_output
        self.dis3.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value.strip(), '#####\n#####\n#####\n#####\n#####')
    
    def test_Ddisplay(self):
        """Test the display part D"""

        capture_output = StringIO()
        sys.stdout = capture_output
        self.dis5.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value.strip(), '##\n##\n##\n##\n##\n##\n##')

    def test_Estr_update(self):
        """Test the display part E"""

        self.assertEqual(self.dis2.__str__(), "[Rectangle] (9) 32/54 - 4/8")
        self.dis2.update(89)
        self.assertEqual(self.dis2.__str__(), "[Rectangle] (89) 32/54 - 4/8")
        self.dis2.update(34, 45)
        self.assertEqual(self.dis2.__str__(), "[Rectangle] (34) 32/54 - 45/8")
        self.dis2.update(2, 9, 1)
        self.assertEqual(self.dis2.__str__(), "[Rectangle] (2) 32/54 - 9/1")
        self.assertEqual(self.dis4.__str__(), "[Rectangle] (88) 0/0 - 10/10")
        self.dis4.update(5, 10, 4, 9)
        self.assertEqual(self.dis4.__str__(), "[Rectangle] (5) 9/0 - 10/4")
        self.dis4.update(2, 11, 4, 10, 450)
        self.assertEqual(self.dis4.__str__(), "[Rectangle] (2) 10/450 - 11/4")
        self.assertEqual(self.dis6.__str__(), "[Rectangle] (1) 1/1 - 1/1")

    def test_Estr_update_2(self):
        """Test the display part E"""

        self.dis2.update(id=89)
        self.assertEqual(self.dis2.__str__(), "[Rectangle] (89) 32/54 - 4/8")
        self.dis2.update(x=34, y=45)
        self.assertEqual(self.dis2.__str__(), "[Rectangle] (89) 34/45 - 4/8")
        self.dis2.update(width=2, height=9, x=1)
        self.assertEqual(self.dis2.__str__(), "[Rectangle] (89) 1/45 - 2/9")
        self.dis2.update(5, 10, id=4, width=9)
        self.assertEqual(self.dis2.__str__(), "[Rectangle] (5) 1/45 - 10/9")
        self.dis2.update(y=2, width=11, height=4, x=10, id=450)
        self.assertEqual(self.dis2.__str__(), "[Rectangle] (450) 10/2 - 11/4")
        self.dis2.update(y=2, width=12)
        self.assertEqual(self.dis2.__str__(), "[Rectangle] (450) 10/2 - 12/4")

    def test_Fdisplay(self):
        """Test the display part F"""

        capture_output = StringIO()
        sys.stdout = capture_output
        self.dis7.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value.strip(), '###\n  ###\n  ###\n  ###\n  ###')
    
    def test_Gdisplay(self):
        """Test the display part G"""

        capture_output = StringIO()
        sys.stdout = capture_output
        self.dis8.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value.strip(), '####\n ####\n ####\n ####')

    def test_Hdisplay(self):
        """Test the display part H"""

        capture_output = StringIO()
        sys.stdout = capture_output
        self.dis9.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value.strip(), '#####\n#####\n#####')


class TestGDictionary(unittest.TestCase):
    """Test dictionary conversion"""

    def test_ATo_dictionary(self):
        """Test the dictionary conversion method"""

        val = Rectangle(4, 9, 2, 0)
        value2 = val.to_dictionary()

        self.assertEqual(value2['width'], 4)
        self.assertEqual(value2['height'], 9)
        self.assertEqual(value2['x'], 2)
        self.assertEqual(value2['y'], 0)

class TestHjsonstring(unittest.TestCase):
    """Test Json String class"""

    def test_AJsonString(self):
        """test that confirms serilization to json string"""
        
        dictionary = {"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}
        json_dict = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dict, str)
        self.assertTrue('x' in json_dict)
        self.assertTrue('y' in json_dict)
        self.assertTrue('width' in json_dict)
        self.assertTrue('height' in json_dict)
        self.assertTrue('id' in json_dict)

        dict_json = Rectangle.from_json_string(json_dict)

        self.assertIsInstance(dict_json[0], dict)
        self.assertEqual(dict_json[0]['height'], 7)
        self.assertEqual(dict_json[0]['width'], 10)
        self.assertEqual(dict_json[0]['x'], 2)
        self.assertEqual(dict_json[0]['y'], 8)
        
    def test_BJsonString(self):
        """Test that confirms serialization to json string"""

        dict_json2 = Rectangle.from_json_string(None)
        self.assertIsInstance(dict_json2, list)
        self.assertEqual(len(dict_json2), 0)

        json_dict3 = Base.to_json_string(None)
        self.assertIsInstance(json_dict3, str)
        self.assertTrue("[]" in json_dict3)
        
        dict_json2 = Rectangle.from_json_string('[]')
        self.assertIsInstance(dict_json2, list)
        self.assertEqual(len(dict_json2), 0)

        json_dict3 = Base.to_json_string([])
        self.assertIsInstance(json_dict3, str)
        self.assertTrue("[]" in json_dict3)


if __name__ == '__main__':
    unittest.main()
