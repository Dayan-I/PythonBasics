class Road:
    def __init__(self, l, w):
        self.__length= l
        self.__width = w

    def mass_road(self):
        return(f'{self.__length * self.__width * 25 * 5} т.')


a = Road(4, 6)
print(a.mass_road())
