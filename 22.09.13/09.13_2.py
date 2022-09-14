class Calc():
    def __init__(self, a, b):
        self.a = int(input())
        self.b = int(input())

    def plus(self):
        return self.a + self.b

    def minus(self):
        return self.a - self.b

    def multiple(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b

calc = Calc(20, 10)

print(calc.plus())
print(calc.minus())
print(calc.multiple())
print(calc.divide())