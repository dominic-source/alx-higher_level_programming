import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import sys
from io import StringIO

class TestAsquareclass(unittest.TestCase):
    """This class will test the square class"""

    def setUp(self):
            """Set up the square class"""
        self.square1 = Square(4, 6)
        self.square2 = Square(2, 2, 5)
        self.square3 = Square(5)
    
    def tearDown(self):
        """Tear down the square class"""
        del self.square1
        del self.square2
        del self.square3

    def test_Aarea(self):
        """Test the area"""

        self.assertEqual(self.square1.area(), 16)
        self.assertEqual(self.square2.area(), 4)
        self.assertEqual(self.square3.area(), 25)
    
    def test_Bdisplay(self):
        """Test the display"""
        capture_output = StringIO()
        sys.stdout = capture_output
        self.square1.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value, '      ####\n      ####\n      ####\n      ####\n')
    
    def test_Cdisplay(self):
        """Test the display"""
        
        capture_output = StringIO()
        sys.stdout = capture_output
        self.square2.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value, '\n\n\n\n\n  ##\n  ##\n')
    
    def test_Ddisplay(self):
        """Test the display"""
        capture_output = StringIO()
        sys.stdout = capture_output
        self.square3.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value, '#####\n#####\n#####\n#####\n#####\n')


class TestBsquareInheritance(unittest.TestCase):
    """Test for inheritance"""

    def test_Ainherit(self):
        """Test inheritance"""

        self.assertTrue(issubclass(Square, Base))
    
    def test_Binstance(self):
        """Test instance"""

        rect = Square(4, 5, 6)
        self.assertFalse(isinstance(rect, Rectangle))
        self.assertTrue(isinstance(rect, Base))


class TestCDisplay(unittest.TestCase):
    """Test the display method"""

    def setUp(self):
        """Set up the display testing"""

        self.dis1 = Square(1, 1)
        self.dis4 = Square(10, 10)
        self.dis5 = Square(2, 7)

        self.dis2 = Square(4, 8, 32, 9)

    def tearDown(self):
        """Tear down the display testing"""

        del self.dis1
        del self.dis4
        del self.dis5
        del self.dis2
   
    def test_Adisplay(self):
        """Test the display method"""

        string = '          ##########\n          ##########\n          ##########\n          ##########\n          ##########\n'
        string += '          ##########\n          ##########\n          ##########\n          ##########\n          ##########\n'

        capture_output = StringIO()
        sys.stdout = capture_output
        self.dis4.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value, string)

    def test_Bdisplay(self):
        """Test the display part B"""
        
        capture_output = StringIO()
        sys.stdout = capture_output
        self.dis1.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value, ' #\n')
    
    def test_Ddisplay(self):
        """Test the display part D"""

        capture_output = StringIO()
        sys.stdout = capture_output
        self.dis5.display()
        sys.stdout = sys.__stdout__
        stdout_value = capture_output.getvalue()
        self.assertEqual(stdout_value, '       ##\n       ##\n')

    def test_Estr_update(self):
        """Test the display part E"""

        self.assertEqual(self.dis2.__str__(), "[Square] (9) 8/32 - 4")
        self.dis2.update(89)
        self.assertEqual(self.dis2.__str__(), "[Square] (89) 8/32 - 4")
        self.dis2.update(34, 45)
        self.assertEqual(self.dis2.__str__(), "[Square] (34) 8/32 - 45")
        self.dis2.update(size=5, x=1)
        self.assertEqual(self.dis2.__str__(), "[Square] (34) 1/32 - 5")
        self.dis2.update(5, 10, id=4, size=9)
        self.assertEqual(self.dis2.__str__(), "[Square] (5) 1/32 - 10")
        self.dis2.update(y=2, size=11, x=10, id=450)
        self.assertEqual(self.dis2.__str__(), "[Square] (450) 10/2 - 11")


class TestDsizeSquare(unittest.TestCase):
    """Test the size of the the square"""

    def test_Asize(self):
        """Test the size of the square"""

        square1 = Square(5)
        square2 = Square(7, 8)
        square3 = Square(4, 3, 7)
        
        self.assertEqual(square1.size, 5)
        self.assertEqual(square2.size, 7)
        self.assertEqual(square3.size, 4)
    
    def test_Aexcept(self):
        """Test if it exception arises"""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square4 = Square("5")
        
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square5 = Square([5])

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square6 = Square({"saf": 5})
        
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            square7 = Square((5, 9), 8)

    def test_Bexcept(self):
        """Test if an exception arises"""

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square10 = Square(8, "5", 8)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square11 = Square(4, [5], 9)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square12 = Square(3, {"54": 4})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            square13 = Square(5, ("43", 5))
    
    def test_Cexcept(self):
        """Test if an exception arises"""

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square14 = Square(8, 5, "5", 8)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square15 = Square(4, 5, [5], 9)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square16 = Square(3, 5, {"54": 4})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            square17 = Square(5, 9, ("sa", 5))

    def test_Dexcept(self):
        """Test if an exception arises"""

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square4 = Square(-1)
        
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square5 = Square(-100)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            square8 = Square(0)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            square6 = Square(5, -10, 10)
        
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            square7 = Square(5, 4, -10)


class TestEDictionary(unittest.TestCase):
    """Test the dictionary"""

    def test_Adictionary(self):
        """Test the dictionary"""

        dict1 = Square(10, 5, 3, 9)
        value = dict1.to_dictionary()
        self.assertEqual(value['size'], 10)
        self.assertEqual(value['x'], 5)
        self.assertEqual(value['y'], 3)

