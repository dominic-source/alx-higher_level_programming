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

