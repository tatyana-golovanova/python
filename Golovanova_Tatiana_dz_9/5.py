class Stationery:
    title = None

    def draw(self):
        print('Запуск отрисовки:')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print('Пишем ручкой')


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print('Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        super().draw()
        print('Отмечаем маркером')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
