import time


class TrafficLight:
    __color = 'красный'

    def running(self):
        print(f'Цвет светофора - {self.__color}')
        time.sleep(7)

        self.__color = 'желтый'
        print(f'Цвет светофора - {self.__color}')
        time.sleep(2)

        self.__color = 'зеленый'
        print(f'Цвет светофора - {self.__color}')
        time.sleep(5)

        self.__color = 'красный'


traffic_light = TrafficLight()
traffic_light.running()
