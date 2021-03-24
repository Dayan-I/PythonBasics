class Car:
    speed = 80
    color = 'red'
    name = 'a'
    is_police = False

    def go(self):
        print('Car start moving')

    def stop(self):
        print('Car stopped moving')

    def turn(self, direction):
        print(f'Car turned {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Speed is too high')
        else:
            print(self.speed)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Speed is too high')
        else:
            print(self.speed)


class SportCar(Car):
    pass


class PoliceCar(Car):
    is_police = True


a = TownCar()
a.show_speed()
