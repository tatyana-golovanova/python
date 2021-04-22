class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print(f'машина повернула {direction}')

    def show_speed(self):
        print(f'скорость машины - {self.speed}')


class TownCar(Car):
    speed = 70
    name = 'городской'
    is_police = False

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('превышение скорости')


class SportCar(Car):
    speed = 120
    name = 'спортивный'
    is_police = False


class WorkCar(Car):
    speed = 50
    name = 'рабочий'
    is_police = False

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('превышение скорости')


class PoliceCar(Car):
    speed = 130
    name = 'полицейский'
    is_police = True


town = TownCar()
town.show_speed()
town.go()
town.turn('вправо')
town.stop()

sport = SportCar()
sport.show_speed()

work = WorkCar()
work.show_speed()

police = PoliceCar()
police.show_speed()
