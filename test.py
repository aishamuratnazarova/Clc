import unittest

from main import Calculator, EngineeringCalculator, ProgrammerCalculator

class Test_TestOperations(unittest.TestCase):
    def test_Add(self):
        num1 = 2
        num2 = 2
        c = Calculator(num1, num2)
        expected_output = 4
        output = c.Add()
        self.assertEqual(output, expected_output)

    def test_Subtract(self):
        num1 = 2
        num2 = 2
        c = Calculator(num1, num2)
        expected_output = 0
        output = c.Subtract()
        self.assertEqual(output, expected_output)

    def test_Divide(self):
        num1 = 2
        num2 = 2
        c = Calculator(num1, num2)
        expected_output = 1
        output = c.Divide()
        self.assertEqual(output, expected_output)

    def test_Modulo(self):
        num1 = 2
        num2 = 2
        c = Calculator(num1, num2)
        expected_output = 0
        output = c.Modulo()
        self.assertEqual(output, expected_output)

    def test_Log(self):
        num1 = 2
        num2 = 2
        c = EngineeringCalculator(num1, num2)
        expected_output = 1.0
        output = c.Log()
        self.assertEqual(output, expected_output)

    def test_Sqrt(self):
        num1 = 4
        num2 = 2
        c = EngineeringCalculator(num1, num2)
        expected_output = 2
        output = c.Sqrt()
        self.assertEqual(output, expected_output)

    def test_Anc(self):
        num1 = 2
        num2 = 2
        c = ProgrammerCalculator(num1, num2)
        expected_output = 2
        output = c.logicalAND()
        self.assertEqual(output, expected_output)

    def test_Or(self):
        num1 = 2
        num2 = 2
        c = ProgrammerCalculator(num1, num2)
        expected_output = 2
        output = c.logicalOR()
        self.assertEqual(output, expected_output)

    def test_Pow(self):
        num1 = 2
        num2 = 2
        c = EngineeringCalculator(num1, num2)
        expected_output = 4
        output = c.Pow()
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()