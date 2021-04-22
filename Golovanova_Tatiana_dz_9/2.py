class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self):
        return self._length * self._width * 0.025 * 5


road = Road(20, 5000)
print(road.calculate_weight())
