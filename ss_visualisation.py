"""Масштабирование объектов на экран"""

# Основано на solar_vis.py Хирьянова

WW = 1200  # Высота окна
WH = 675  # Длина окна
scale = None  # Масштаб


def set_scale(d, k):
    """
    Вычисляет и устанавливает значение масштаба
    :param d: Максимальное расстояние между объектами симуляции
    :param k: Коэффициент, отвечающий за визуальное приближение и отдаление объектов
    """
    global scale
    scale = k * min(WW, WH) / d


def screen_x(x):
    """
    :param x: Координата объекта по оси Х
    :return: Координата объекта на экране по оси Х
    """
    return x * scale + WW // 2


def screen_y(y):
    """
    :param y: Координата объекта по оси Y
    :return: Координата объекта на экране по оси Y
    """
    return y * scale + WH // 2


def draw_star(canvas, star):
    """
    Создаёт объект звезды на холсте и инициализирует
    переменную у соответствующего экземпляра класса этим объектом
    :param canvas: Холст
    :param star: Экземпляр звезды
    """
    x = screen_x(star.x)
    y = screen_y(star.y)
    r = star.R
    star.im = canvas.create_oval([x - r, y - r], [x + r, y + r], fill=star.color)


def draw_planet(canvas, planet):
    """
    Создаёт объект планеты на холсте и инициализирует
    переменную у соответствующего экземпляра класса этим объектом
    :param canvas: Холст
    :param planet: Экземпляр планеты
    """
    x = screen_x(planet.x)
    y = screen_y(planet.y)
    r = planet.R
    planet.im = canvas.create_oval([x - r, y - r], [x + r, y + r], fill=planet.color)


def move_object(canvas, obj):
    """
    Перемещение объекта на холсте в
    соответствии с его физическими координатами
    :param canvas: Холст
    :param obj: объект
    """
    x = screen_x(obj.x)
    y = screen_y(obj.y)
    r = obj.R
    canvas.coords(obj.im, x - r, y - r, x + r, y + r)


if __name__ == '__main__':
    print('This module is not to run the program')
