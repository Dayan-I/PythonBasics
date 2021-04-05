class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return f'{self.real + other.real}+{self.imaginary + other.imaginary}i'

    def __mul__(self, other):
        return f'{self.real * other.real - (self.imaginary * other.imaginary)}+{self.imaginary + other.imaginary}i'


z = Complex(5, 7)
zz = Complex(4, 6)
print(z + zz)
print(z * zz)
