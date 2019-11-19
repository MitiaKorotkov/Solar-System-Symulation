"""Работа с файлом с данными"""

# Основано на solar_input.py Хирьянова


from ss_objects import Star, Planet


def init_space_objects(data_filename):
    """
    Считывает данные об объектах симуляции из данного
    файла и создаёт для них объекты, массив с которыми возвращается.
    Может возникнуть ошибка NameError при наличии в файле объекта
    с именем отличным от 'planet' или 'star'
    :param data_filename: Имя файла с данными
    :return: Массив объектов, описанных в файле
    """
    objects = []  # Массив объектов симуляции
    # Открытие файла
    with open(data_filename) as f:
        # Считывание данных и приведение их к желаемому виду
        for line in f:
            if len(line.strip()) == 0 or line[0] == '#':
                continue
            obj = line.split()[0].lower()
            # Создание требуемых объектов с требуемыми параметрами
            if obj == 'star':
                star = Star(float(line.split()[3]), float(line.split()[4]), float(line.split()[5]),
                            float(line.split()[6]),
                            float(line.split()[7]), int(line.split()[1]), line.split()[2])
                objects.append(star)
            elif obj == 'planet':
                planet = Planet(float(line.split()[3]), float(line.split()[4]), float(line.split()[5]),
                                float(line.split()[6]),
                                float(line.split()[7]), float(line.split()[1]), line.split()[2])
                objects.append(planet)
            else:
                raise NameError('Unknown object')
    return objects


def save_data_to_file(data_filename, objects):
    """
    Записывает в файл данные о телах, участвующих в симуляции
    :param data_filename: Имя файла для записи
    :param objects: Массив тел, данные о которых нужно записать
    """
    pass

if __name__ == '__main__':
    print('This module is not to run the program')
