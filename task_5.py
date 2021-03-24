class Stationery:
    title = 'some'
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Переопределили метод для {self}')

class Pencil(Stationery):
    def draw(self):
        print(f'Переопределили метод для {self}')

class Handle(Stationery):
    def draw(self):
        print(f'Переопределили метод для {self}')
