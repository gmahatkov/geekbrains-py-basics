"""
Задача 1
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
"""
from random import randint


class Matrix:
    def __init__(self, *args):
        if not all(map(lambda x: type(x) is list, args)):
            raise TypeError('Wrong constructor argument type - expects list')
        cols = len(args[0])
        if not all(map(lambda x: len(x) == cols, args)):
            raise ValueError('All arguments must be of the same length (length of first argument)')
        self.__matrix = list(args)
        pass

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'Expects right operand to be instance of Matrix, got {type(other)}')
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f'Right operand must have the same size '
                             f'expects: {self.cols}X{self.rows}, got: {other.cols}X{other.rows}')
        args = [[None] * self.cols] * self.rows
        for row_idx, row in enumerate(self.__matrix):
            for col_idx, col in enumerate(row):
                args[row_idx][col_idx] = col + other.__matrix[row_idx][col_idx]
        return Matrix(*args)

    def __str__(self):
        self_str = ''
        for row in self.__matrix:
            self_str += str(row).strip('[]') + '\n'
        return self_str

    @property
    def rows(self):
        return len(self.__matrix)

    @property
    def cols(self):
        return len(self.__matrix[0])


if __name__ == '__main__':
    matrix1 = Matrix([1, 1], [1, 1])
    matrix2 = Matrix([2, 2], [2, 2])
    matrix3 = Matrix([4, 5, 6], [1, 2, 3])
    matrix4 = Matrix([2, 4, 5], [8, 2, 7])
    try:
        print(matrix1 + matrix2)
        print(matrix1 + matrix3)
        print(matrix4 + matrix3)
    except ValueError as e:
        print(e)
    except TypeError as e:
        print(e)
