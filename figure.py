class BaseFigure:
    """ Методы и переменные геометрических фигур"""

    angles = None
    name = None
    perimeter = None
    area = None

    def add_square(self, other_figure):
        """ Метод возвращает сумму площадей двух геометрических фигур"""

        if isinstance(other_figure, BaseFigure):
            sum_areas = self.area + other_figure.area
            return sum_areas
        else:
            return 'Передан неверный класс геометрической фигуры'

    def get_angles(self, figure):
        """ Метод возвращает количество углов геометрической фигуры"""

        return figure.angles

    def get_name(self, figure):
        """ Метод возвращает количество название геометрической фигуры"""

        return figure.name
