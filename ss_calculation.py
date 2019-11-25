# Написано Алехиной Дарьей feat. Дмитрий Коротков

G = 6.67E-11  # Гравитационная постоянная


def set_force_value(obj, objects):
    """
    Вычисляет и устанавливает значение силы,
    действующей на тело со стороны всех остальных тел
    :param obj: Тело
    :param other_obj: Тела, участвующие во взаимодействии
    """
    obj.fx = 0
    obj.fy = 0
    for j in range (len(objects)):
        if obj != objects[j]:
            obj.fx -= (obj.x-objects[j].x)*\
                     G*obj.m*objects[j].m/(((obj.x-objects[j].x)**2+(obj.y-objects[j].y)**2)**(3/2))
    for j in range (len(objects)):
        if obj != objects[j]:
            obj.fy -= (obj.y-objects[j].y)*\
                     G*obj.m*objects[j].m/(((obj.x-objects[j].x)**2+(obj.y-objects[j].y)**2)**(3/2))


def move_object(obj, dt):
    """
    Пересчёт и установка значений скорости и
    координат в соответствии с заданной силой
    :param obj: Тело
    :param dt: Промежуток времени
    """
    obj.vx+=dt*(obj.fx/obj.m)
    obj.vy+=dt*(obj.fy/obj.m)
    obj.x+=dt*obj.vx
    obj.y+=dt*obj.vy
    


def set_objects_position(objects, dt):
    """
    Перемещает объекты на холсте в соответствии
    с заданными координатами
    :param objects: Тела
    :param dt: Промежутой Времени
    
    """
    for i in range(len(objects)):
        set_force_value(objects[i], objects)
    for i in range(len(objects)):
       move_object(objects[i],dt)

if __name__ == '__main__':
    print('This module is not to run the program')
