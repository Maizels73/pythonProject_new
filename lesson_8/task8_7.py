class ComplNumb:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def look(self):
        zn_imag = "+"

        if self.imag < 0:
            zn_imag = ""
        return f"compl_number = ({self.real}{zn_imag}{self.imag}j)"

    def __add__(self, other):
        r1 = self.real
        i1 = self.imag
        r2 = other.real
        i2 = other.imag
        print(f"{r1} + {r2} and {i1} + {i2}")
        test3 = ComplNumb (r1 + r2, i1 + i2)
        return ComplNumb.look(test3)


test = ComplNumb(2,-3)
test1 = ComplNumb(4,-6)
print(ComplNumb.look(test))
print(ComplNumb.look(test1))

test2 = test + test1
print(test2)