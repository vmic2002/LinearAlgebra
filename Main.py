#in this file can solve linear systems and can find inverse of matrices
#from AugmentedMatrix import *
from AugmentedMatrix import *
"""
#to solve linear system:
rows = [[2, 3, 1, 2], [1, 4, 5, 6], [1, 6, 3, 5]]
m = AugmentedMatrix(Matrix(rows), False) #False for linear system
m.solve()
"""

"""
#to find inverse of matrix
square = [[2, 7, 1], [1, 4, -1], [1, 3, 0]]
m1 = Matrix(square)


m1Inverse = Matrix.inverse(m1)
m1Inverse.printMatrix()
"""

# matrix algebra
m2 = Matrix([[1, 2, 3], [4, 5, 6]])
m3 = Matrix([[7, 8], [9, 10], [11, 12]])

sumMatrix = Matrix.multiply(m2, m3)
m2.printMatrix()
print("*")
m3.printMatrix()
print("=")
sumMatrix.printMatrix()
