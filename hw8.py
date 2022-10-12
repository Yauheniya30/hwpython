# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать
# число, месяц,
# год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date:
    def __init__(self, dd_mm_yyyy):
        self.date = dd_mm_yyyy

    @classmethod
    def set_day(cls, obj):
        day = obj.date.split('-')
        return day[0], day[1], day[2]

    @classmethod
    def __getitem__(cls, item):
        return cls.set_day

    @staticmethod
    def validace(day):
        if 1 <= day[0] <= 30:
            if 1 <= day[1] <= 12:
                if day[1] == 1:
                    print('january')
                if day[1] == 2:
                    print('february')
                if day[1] == 3:
                    print('march')
                if day[1] == 4:
                    print('april')
                if day[1] == 5:
                    print('may')
                if day[1] == 6:
                    print('june')
                if day[1] == 7:
                    print('july')
                if day[1] == 8:
                    print('august')
                if day[1] == 9:
                    print('september')
                if day[1] == 10:
                    print('october')
                if day[1] == 11:
                    print('november')
                if day[1] == 12:
                    print('december')
                    if 1900 <= day[2] <= 2030:
                        print('year:')
                    else:
                        print('no year')
                else:
                    print('No month')
            print('month:')
        else:
            print('No month')
        print(day[0] + day[1] + day[2])


day_month_year = Date('15-6-2022')
print(Date.set_day(day_month_year))
print(Date.validace(day_month_year))

#
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию
# и не завершиться с ошибкой.


class Divzero(Exception):

    def __init__(self, res):
        self.res = res


num1 = int(input('enter a:'))
num2 = int(input('enter b:'))

try:
    res = num1 / num2
    if num2 == 0:
        raise Divzero('division by zero')
except(ZeroDivisionError, Divzero) as err:
    print(err)
else:
    print(res)
finally:
    print('end')


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.


class Er(Exception):
    def __init__(self, my_list):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('Enter the number'))
                self.my_list.append(val)
                if val == 77:
                    print(f'{self.my_list}')
                    print('stop')
                    break
            except(ValueError, TypeError, Er) as err:
                print(err)
            else:
                print(f'{self.my_list}')
            finally:
                print('end')


er = Er(1)
print(er.my_input())


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.


class Officeequipment:
    new = 'new'
    broken = 'broken'
    used = 'used'

    def __init__(self, new, broken, used):
        self.new = new
        self.broken = broken
        self.used = used

    def exploitation(self):
        return self.new, self.used, self.broken


equipment = Officeequipment(new='20', broken='5', used='25')


class Technique(Officeequipment):
    printer = 'printer'
    scanner = 'scanner'
    xerox = 'xerox'
    price1 = 'price1: 50$ - 100$'
    price2 = 'price2: 100 - 250$'
    price3 = 'price3: 250 - 500$'

    def __init__(self, new, broken, used, printer, scanner, xerox):
        super().__init__(new, broken, used)
        self.printer = printer
        self.scanner = scanner
        self.xerox = xerox

    @classmethod
    def prise(cls, price1, price2, price3):
        cls.price1 = price1
        cls.price2 = price2
        cls.price3 = price3
        return f'{cls.price1 }, {cls.price2}, {cls.price3}'

    @property
    def count_in_storage(self):
        return self.count_in_storage

    @count_in_storage.setter
    def count_in_storage(self, value):
        if value > 0:
            self.count_in_storage = count
            input('Enter count of technique:')
        else:
            print('Not available')


count = Technique(new='20', broken='5', used='25', printer='16', scanner='14', xerox='8')


class Orgtechnique(Technique):
    floor_place = 'placement: floor_place'
    desc_place = 'placement desc_place'
    color = 'color print'
    black_white = 'black_white'

    @classmethod
    def info(cls):
        print(cls.floor_place, cls.desc_place)

    @classmethod
    def info_color(cls, color, black_white):
        cls.color = color
        cls.black_white = black_white
        return f'{cls.color}, {cls.black_white}'


class Printer(Orgtechnique):

    def __init__(self, new, broken, used, price1, price2, price3, laser, led, jet, matrix):
        super().__init__(new, broken, used, price1, price2, price3)
        self.laser = laser
        self.led = led
        self.jet = jet
        self.matrix = matrix

    @staticmethod
    def info_black_white(obj):
        return f'black_white: {obj.black_white}, {obj.color}'

    def info(self):
        return self.laser, self.led, self.jet, self.matrix


class Scanner(Orgtechnique):

    def __init__(self, new, broken, used, price1, price2, price3, hand_held, desktop):
        super().__init__(new, broken, used, price1, price2, price3)
        self.hh = hand_held
        self.desc = desktop

    def info(self):
        return self.hh, self.desc


class Xerox(Orgtechnique):
    def __init__(self, new, broken, used, price1, price2, price3, digital, analog):
        super().__init__(new, broken, used, price1, price2, price3)
        self.digital = digital
        self.analog = analog

    def info(self):
        return self.digital, self.analog

    def __repr__(self):
        return self.digital + self.analog + self.new + self.broken + self.used


xerox1 = Xerox(new='2', broken='0', used='4', price1='1', price2='3', price3='1', digital='1', analog='3')


date = Orgtechnique(20, 5, 25, 16, 14, 8)
print(date.__dict__)

date1 = Xerox(2, 0, 4, 1, 3, 1, 1, 3)
print(date1.__dict__)


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + bi'

    def __add__(self, other):
        return f'z = {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'z = {(self.a * other.a) - (self.b * other.b)} + {(self.b * other.a) + (self.a * other.b)}i'

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


z1 = ComplexNumber(-6, -13)
z2 = ComplexNumber(3, 8)
print(z1 + z2)
print(z1 * z2)

