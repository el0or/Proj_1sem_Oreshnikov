#создайте класс матрица, который имеет атрибуты колличества строк и столбцов . добавьте методы сложения, вычитания и умножения матриц
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    def add(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
            return result
        else:
            return None

    def subtract(self, other):
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
            return result
        else:
            return None

    def multiply(self, other):
        if self.cols == other.rows:
            result = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return result
        else:
            return None

    def __str__(self):
        return '\n'.join([' '.join([str(item) for item in row]) for row in self.matrix])

m1 = Matrix(2, 2)
m1.matrix = [[1, 2], [3, 4]]

m2 = Matrix(2, 2)
m2.matrix = [[5, 6], [7, 8]]

print("\nМатрица 1:")
print(m1)

print("\nМатрица 2:")
print(m2)

print("\nСумма матриц:")
print(m1.add(m2))

print("\nВычитание матриц:")
print(m1.subtract(m2))

m3 = Matrix(2, 3)
m3.matrix = [[1, 2, 3], [4, 5, 6]]
m4 = Matrix(3, 2)
m4.matrix = [[7, 8], [9, 10], [11, 12]]

print("\nМатрица 3:")
print(m3)

print("\nМатрица 4:")
print(m4)

print("\nУмножение матриц:")
print(m3.multiply(m4))