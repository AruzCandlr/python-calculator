import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-5, 4), -1)
        self.assertEqual(self.calc.add(-5, 5), 0)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, -2), 4)
        self.assertEqual(self.calc.subtract(2, 2), 0)


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(3, 6), 18)
        self.assertEqual(self.calc.multiply(0, 6), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 2), 2)
        self.assertEqual(self.calc.divide(9, 9), 1)
        self.assertEqual(self.calc.divide(0, 9), 0)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(5,2), 1)
        self.assertEqual(self.calc.modulo(4,2), 0)




    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()