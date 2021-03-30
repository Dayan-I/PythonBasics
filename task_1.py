class Matrix:
    def __init__(self, _list):
        self._list = _list

    def __str__(self):
        return '\n'.join('\t'.join([str(el) for el in i]) for i in self._list)


    def __add__(self, other):
        try:
            return Matrix([
                [self._list[i][j] + other._list[i][j] for j in range(len(self._list[0]))]
                for i in range(len(other._list))])
        except IndexError:
            return f'Matrices must be same sized'


