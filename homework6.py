# 1. Создать класс TrafficLight (светофор). определить у него один атрибут color (цвет) и метод running (запуск);
#     атрибут реализовать как приватный;в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
#     зелёный;продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
#     третьего (зелёный) — на ваше усмотрение; переключение между режимами должно осуществляться только в указанном
#     порядке (красный, жёлтый, зелёный); проверить работу примера, создав экземпляр и вызвав описанный метод.

# class TrafficLight:
#     color1 = 'stop'
#     color2 = 'get ready'
#     color3 = 'going'
#     time = 'waiting'
#
#     def light_info(self):
#         self.color1 = color1
#         self.color2 = color2
#         self.color3 = color3
#         self.time = time
#         return f'color1: {self.color1} color2: {self.color2} color3: {self.color3} time {self.time}'
#
#
# color1 = TrafficLight()
# time = TrafficLight()
# print('stop', 'red')
# print('waiting 7s')
#
# color2 = TrafficLight()
# print('get ready', 'yellow')
# print('waiting 2s')
#
# color3 = TrafficLight()
# print('going', 'green')
# print('waiting 7s')
# *********************************************************************************************************

# 2. Реализовать класс Road (дорога). определить атрибуты: length (длина), width (ширина);
#     значения атрибутов должны передаваться при создании экземпляра класса;
#     атрибуты сделать защищёнными;
#     определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#     использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
#     толщиной в 1 см*число см толщины полотна;
#     проверить работу метода.Например: 20 м*5000 м*25 кг*5 см = 12500 т.

#
# m = 25
# h = 5
#
#
# class Road:
#
#     length = int(input())
#     width = int(input())
#
#     def set_into(self):
#         self.length = int(input())
#         self.width = int(input())
#
#     def total(self):
#         return f'  total =  {(m * h * self.length * self.width) / 1000}'
#
#
# road1 = Road()
# print(road1.total(), 't')


# 3. Реализовать базовый класс Worker (работник).
#     определить атрибуты: name, surname, position (должность), income (доход);
#     последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
#     {"wage": wage, "bonus": bonus};
#     создать класс Position (должность) на базе класса Worker;
#     в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
#     и дохода с учётом премии (get_total_income);
#     проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
#     проверить значения атрибутов, вызвать методы экземпляров.

# class Worker:
#
#     name = 'Petr'
#     surname = 'Petrov'
#     position = 'employer'
#
#     def set_info(self, name, surname, position):
#         self.name = name
#         self.surname = surname
#         self. position = position
#
#
# worker1 = Worker()
# print(worker1.name)
# print(worker1.surname)
# print(worker1.position)
#
#
# class Position:
#     name2 = 'Petr Nikolaevich Petrov'
#     wage = int(input('Enter wage:'))
#     bonus = int(input('Enter bonus:'))
#     sum_income = wage + bonus
#
#     def get_full_name(self):
#         return f'{self.name2}'
#
#     def get_total_income(self, wage, bonus):
#         self.sum_income = {"wage": wage, "bonus": bonus}
#         return f'{self.sum_income}'
#
#
# worker = Position()
# print(worker.name2)
# print(worker.sum_income)


# 4. Реализуйте базовый класс Car.
#  у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
#     turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#     опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#     добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#     для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
#     и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
#
# class Car:
#
#     def __init__(self, name, speed, color, direction, police=False):
#         print()
#         self.name = name
#         self.speed = speed
#         self.color = color
#         self.police = police
#         self.direction = direction
#
#     def go(self):
#         return f'car: {self.name} going'
#
#     def stop(self):
#         return f'car: {self.name} stopping'
#
#     def turn(self):
#         return f'car: {self.name} turned {"left" if {self.direction} == 0 else "right"}'
#
#     def show_speed(self):
#         return f'car {self.name} {self.color} {self.speed}'
#
#
# class TownCar:
#
#     def __init__(self):
#         self.speed = int(input('enter km/h:'))
#         print(f' car: {"speed is Ok" if {self.speed} < 60 else " over speed"}')
#
#
# class SportCar:
#
#     def __init__(self, sport):
#         self.sport = sport
#         print(f'car: {self.sport}')
#
#
# class WorkCar:
#
#     def speed(self):
#         return f' car: {"speed is Ok" if {self.speed} < 40 else " over speed"}'
#
#
# class PoliceCar:
#     def __init__(self, name, color, speed, police=True):
#         super().__init__(name, color, speed, police)
#
#
# car1 = Car('opel', '90 km/ h', 'black', 'going direction')
# print(car1.name)
# print(car1.speed)
# print(car1.color)
# print(car1.direction)


# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное
# сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

# class Stationery:
#
#     title = 'Gamma'
#     draw = 'pencil drawing'
#
#     def set_info(self, title, draw):
#         self.title = title
#         self.draw = draw
#         print(f'«Запуск отрисовки»: {self.title} {self.draw}')
#
#
# class Pen(Stationery):
#     def pen(self):
#         print(f'«Запуск отрисовки»:{self.title} {self.draw}')
#
#
# class Pencil(Stationery):
#     def pencil(self):
#         print(f'«Запуск отрисовки»:{self.title} {self.draw}')
#
#
# class Handle(Stationery):
#     def handle(self):
#         print(f'«Запуск отрисовки»:{self.title} {self.draw}')
#
#
# stationery1 = Stationery()
# print(stationery1.title)
# print(stationery1.draw)
