class C1:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print("A1 = ", self.a)
        print("B1 = ", self.b)

    def average(self):
        print('A + B = ', self.a+self.b)


class C2(C1):

    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.c = c
        self.d = d

    def display(self):
        print("A2 = ", self.a)
        print("B2 = ", self.b)
        print("C = ", self.c)
        print("D = ", self.d)


obj1 = C1(1, 2)
obj1.display()

obj2 = C2(10, 20, 30, 40)
obj2.average()
obj2.display()
