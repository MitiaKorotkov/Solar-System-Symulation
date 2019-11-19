"""Координация и организация работы программы"""

# Написано Коротковым Дмитрием


import tkinter
import tkinter.filedialog
import ss_calculation as ssc
import ss_visualisation as ssv
import ss_input as ssi

time = 0  # Время с начала симуляции
scale_v = None  # Коэффициент, отвечающий за визуальное приближение и отдаление объектов
pause_button = None  # Кнопка старт/пауза
speed = None  # Скорость симуляции
canvas = None  # Холст
delta_t = None  # Время между пересчётом координат
flag = False  # Переменная отвечающая за старт/остановку симуляции
objects = []  # Массив объектов, участвующих в симуляции


def update():
    """
    Обновляет холст, если симуляция запущена
    """
    global time, speed, scale_v
    # Начальное расположение объектов на холсте
    max_d = max([max(abs(i.x), abs(i.y)) for i in objects])
    ssv.set_scale(max_d, 0.5 + scale_v.get())
    ssc.set_objects_position(objects, delta_t.get())
    # Перемещение объектов
    for i in objects:
        ssv.move_object(canvas, i)
    # Изменение физического времени
    time += delta_t.get()
    # Проверка на старт/остановку симуляции
    if flag:
        canvas.after(101 - int(speed.get()), update)


def start_update():
    """
    Обработка нажатия на кнопку 'Start'
    """
    global flag, pause_button
    # Симуляция запущена
    flag = True
    # Изменение кнопки старат на кнопку паузы
    pause_button['text'] = 'Pause'
    pause_button['command'] = pause_update
    # Запуск симуляции
    update()


def pause_update():
    """
    Обработка нажатия на кнопку паузы
    """
    global flag, pause_button
    # Симуляция остановлена
    flag = False
    # Изменение кнопки паузы на кнопку старт
    pause_button['text'] = 'Start'
    pause_button['command'] = start_update


def reed_from_file():
    """
    Организует открытие диалога для выбора файла для считывания данных из него.
    Считывает данные и располагает объекты из файла на холсте.
    Может возникнуть ошибка NameError при наличии в файле объекта
    с именем отличным от 'planet' или 'star'
    """
    global objects, flag, canvas
    # Остановка симуляции
    flag = False
    # очистка холста
    for i in objects:
        canvas.delete(i.im)
    # открытие диалога выбора файла
    f = tkinter.filedialog.askopenfilename(filetypes=(('Filename', '.txt'),))
    # Инициализация массива объектов
    objects = ssi.init_space_objects(f)
    # Установка масштаба
    max_d = max([max(abs(i.x), abs(i.y)) for i in objects])
    ssv.set_scale(max_d, 0.5 + scale_v.get())
    # Отрисовка объектов
    for i in objects:
        if i.id == 'star':
            ssv.draw_star(canvas, i)
        elif i.id == 'planet':
            ssv.draw_planet(canvas, i)
        else:
            raise NameError('Unknown object')


def save_to_file():
    """
    Открывает диалог сохранения данных о положении
    объектов в файл и сохраняет данные в выбранный файл
    """
    global objects
    # Открытие файлового диалога
    f = tkinter.filedialog.asksaveasfilename(filetypes=(('Filename', '.txt'),))
    # Сохранение данных в файл
    ssi.save_data_to_file(f, objects)


def main():
    """
    Создание эементов графического дизайна( окно, кнопки, холст, надписи )
    Запуск главного цикла
    """
    global delta_t, canvas, speed, pause_button, scale_v
    root = tkinter.Tk()
    speed = tkinter.DoubleVar()
    scale_v = tkinter.DoubleVar()
    delta_t = tkinter.DoubleVar()
    delta_t.set(1000)

    # Создание холста
    canvas = tkinter.Canvas(root, width=ssv.WW, height=ssv.WH, bg="black")
    canvas.pack(side=tkinter.TOP)
    frame = tkinter.Frame(root)
    frame.pack(side=tkinter.BOTTOM)

    # Создание кнопок
    pause_button = tkinter.Button(frame, text="Start", command=start_update, width=10)
    pause_button.pack(side=tkinter.LEFT)

    # Создание ползунков
    scale = tkinter.Scale(frame, variable=speed, orient=tkinter.HORIZONTAL, width=10)
    scale.pack(side=tkinter.LEFT)
    scale = tkinter.Scale(frame, variable=scale_v, to=40, orient=tkinter.HORIZONTAL, width=10)
    scale.pack(side=tkinter.LEFT)

    # Создание надписей
    label1 = tkinter.Label(text='', padx=220)
    label1.pack(side=tkinter.LEFT)
    label2 = tkinter.Label(text='speed', padx=70, font='Arial 10')
    label2.pack(side=tkinter.LEFT)
    label3 = tkinter.Label(text='scale', font='Arial 10')
    label3.pack(side=tkinter.LEFT)

    # Создание кнопок
    load_file_button = tkinter.Button(frame, text="Open file", command=reed_from_file)
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frame, text="Save to file", command=save_to_file)
    save_file_button.pack(side=tkinter.LEFT)

    # Главный цикл
    root.mainloop()


if __name__ == '__main__':
    main()
