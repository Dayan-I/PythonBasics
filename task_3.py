class Cell:
    def __init__(self, s):
        self.size = s

    def __str__(self):
        return f'{self.size}'

    def __add__(self, other):
        return Cell(self.size + other.size)

    def __sub__(self, other):
        if self.size > other.size:
            return Cell(self.size - other.size)
        else:
            return 'Error'

    def __truediv__(self, other):
        return Cell(self.size // other.size)

    def __mul__(self, other):
        return Cell(self.size * other.size)

    def make_order(self, row):
        return '\n'.join(['*' * row for i in range(self.size // row)]) + '\n' + '*' * (self.size % row)


a = Cell(9)
b = Cell(6)
print(a.make_order(6))
print(a - b)