class area():
    def __init__(self, w, h):
        self.w = w
        self.h = h
        
    def square(self):
        return self.w * self.h

    def triangle(self):
        return self.w * self.h // 2

    def circle(self):
        return (self.w / 2) ** 2 * 3.14

a = area(10, 20)

print(a.square())
print(a.triangle())
print(a.circle())
   