import math


class Calculator:
    num1 = 1
    num2 = 1

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Add(self):
        return self.num1 + self.num2

    def Subtract(self):
        return self.num1 - self.num2

    def Multiply(self):
        return self.num1 * self.num2

    def Divide(self):
        return self.num1 / self.num2

    def Modulo(self):
        return self.num1 % self.num2


class EngineeringCalculator(Calculator):
    num1 = 1
    num2 = 1

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def Log(self):
        return math.log(self.num1, self.num2)

    def Sqrt(self):
        return math.sqrt(self.num1)

    def Pow(self):
        return math.pow(self.num1, self.num2)


class ProgrammerCalculator(Calculator):
    num1 = 1
    num2 = 1

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def logicalAND(self):
        return self.num1 and self.num2

    def logicalOR(self):
        return self.num1 or self.num2


class FibonacciSequence:
    n = 1

    def __init__(self, n):
        self.n = n

    def fib_recursive(self):
        a, b = 0, 1
        while self.n > 0:
            a, b = b, a + b
            self.n -= 1
        return a


class Round:
    n = 1.0

    def __init__(self, n):
        self.n = n

    def Floor(self):
        return math.floor(self.n)

    def Ceil(self):
        return math.ceil(self.n)


class Trigonometry:
    n = 1.0

    def __init__(self, n):
        self.n = n

    def Sin(self):
        return math.sin(self.n)

    def Cos(self):
        return math.cos(self.n)

    def Tan(self):
        return math.tan(self.n)

    def ASin(self):
        return math.asin(self.n)

    def ACos(self):
        return math.acos(self.n)

    def ATan(self):
        return math.atan(self.n)


class Check:
    n = 1.0

    def __init__(self, n):
        self.n = n

    def Fin(self):
        return math.isfinite(self.n)

    def Inf(self):
        return math.isinf(self.n)

    def Nan(self):
        return math.isnan(self.n)


print("Select operation:")
print("1:Add")
print("2.Subtract")
print("3:Multiply")
print("4:Divide")
print("5:Modulo")
print("6:Log")
print("7:Square root")
print("8:Power")
print("9:Logical AND")
print("10:Logical OR")

choice = int(input("Choose operation:"))
num1 = int(input("Enter first number:"))

if choice == 7:
    c1 = EngineeringCalculator(num1, 0)
    print(c1.Sqrt())
else:
    num2 = int(input("Enter second number:"))
    if choice == 1:
        c = Calculator(num1, num2)
        print(c.Add())
    elif choice == 2:
        c = Calculator(num1, num2)
        print(c.Subtract())
    elif choice == 3:
        c = Calculator(num1, num2)
        print(c.Multiply())
    elif choice == 4:
        c = Calculator(num1, num2)
        print(c.Divide())
    elif choice == 5:
        c = Calculator(num1, num2)
        print(c.Modulo())
    elif choice == 6:
        c1 = EngineeringCalculator(num1, num2)
        print(c1.Log())
    elif choice == 8:
        c1 = EngineeringCalculator(num1, num2)
        print(c1.Pow())
    elif choice == 9:
        c2 = ProgrammerCalculator(num1, num2)
        print(c2.logicalAND())
    elif choice == 10:
        c2 = ProgrammerCalculator(num1, num2)
        print(c2.logicalOR())
    else:
        print("Invalid input")