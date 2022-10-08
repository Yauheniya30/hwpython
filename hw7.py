# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.


# class Matrix:
#
#     def __init__(self, p1, p2, p3):
#         self.p1 = p1
#         self.p2 = p2
#         self.p3 = p3
#
#     def __str__(self):
#         self.p1 = ' '.join(map(str, self.p1))
#         self.p2 = ' '.join(map(str, self.p2))
#         self.p3 = ' '.join(map(str, self.p3))
#         return '|' + str(self.p1) + '|' '\n' + '|' + str(self.p2) + '|' + '\n' + '|' + str(self.p3) + '|' '\n'
#
#     def __add__(self, other):
#         suma1 = []
#         suma2 = []
#         suma3 = []
#         for i in range(len(self.p1)):
#             for j in range(len(self.p1[0])):
#                 suma1 = self.p1[i][j] + other.p1[i][j]
#                 [i][j] += 1
#         for i in range(len(self.p2)):
#             for j in range(len(self.p2[0])):
#                 suma2 = self.p2[i][j] + other.p2[i][j]
#                 [i][j] += 1
#         for i in range(len(self.p3)):
#             for j in range(len(self.p3[0])):
#                 suma3 = self.p3[i][j] + other.p3[i][j]
#                 [i][j] += 1
#                 return '|' + suma1 + '|' '\n' + '|' + suma2 + '|' + '\n' + '|' + suma3 + '|' '\n'
#
#
# m = [5, 7, 1], [8, 0, 5], [3, 2, 9]
# a = Matrix([4, 7, 5], [8, 9, 5], [5, 8, 4])
# b = Matrix([5, 7, 1], [8, 0, 5], [3, 2, 9])
# print(a)
# print(b)
# print(a + b)


# /////////////////////////////////////////////////////////////////////////////////////////////


# class Matrix:
#
#     def __init__(self, mtrx):
#         self.mtrx = mtrx
#
#     def __str__(self):
#         for i in range(len(self.mtrx)):
#             zapis = '' + '\t'.join(map(str, self.mtrx[i])) + '\n'
#             return zapis
#
#     def __add__(self, other):
#         for i in range(len(self.mtrx)):
#             for j in range(len(self.mtrx[i])):
#                 res = self.mtrx[i][j] + other.mtrx[i][j]
#                 return Matrix(res)
#
#
# a = Matrix([4, 7, 5], [8, 9, 5], [5, 8, 4])
# b = Matrix([5, 7, 1], [8, 0, 5], [3, 2, 9])
# print(a)
# print(b)
# res = a + b
# print(res)

# ******************************************************************************************************************
# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.


# from abc import ABC
#
#
# class Clothing(ABC):
#
#     def __init__(self, p1, p2):
#         self.__size = p1
#         self.__growth = p2
#
#     @property
#     def total_textil(self):
#         return (self.__size / 6.5 + 0.5) + (2 * self.__growth + 0.3)
#
#     @total_textil.setter
#     def total_textil(self, value):
#         self.__size = value
#         self.__growth = value
#         if self.__size > 60 or self.__size < 38:
#             self.__size = False
#         if self.__growth < 158 or self.__growth > 190:
#             self.__growth = False
#
#
# @property
# class Coat (Clothing):
#     def coat(self):
#         return self.__size / 6.5 + 0.5
#
#
# @property
# class Costume (Clothing):
#     def costume(self):
#         return 2 * self.__growth + 0.3
#
#
# clothing1 = Clothing(46, 160)
# total_textil = property()
# print(clothing1.total_textil)
#
# ******************************************************************************************************************
# 3.3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно.


# class Cell:
#
#     def __init__(self, p1):
#         self.__cell = p1
#         self.simbol = '*'
#
#     def __add__(self, other):
#         return self.__cell.p1 + other.p1
#
#     def get__sub__(self):
#         return self.__cell.p1
#
#     def __sub__(self, other):
#         return self.__cell.p1 - other.p1
#
#     def set__sub__(self, value):
#         if value > 0:
#             self.__cell.p1 = value
#             return
#         else:
#             print('Wrong data')
#
#     def __mul__(self, other):
#         return self.__cell.p1 * other.p1
#
#     def __truediv__(self, other):
#         return self.__cell.p1 // other.p1
#
#     def make_order(self, count):
#         while self.__cell > 0:
#             for i in range(1, count + 1):
#                 print('*', end='')
#                 i -= 1
#                 if self.__cell <= 0:
#                     print('no sense')
#
#
# a = 2
# b = 10
# number = 5
# cell1 = Cell(2)
# cell2 = Cell(10)
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)












