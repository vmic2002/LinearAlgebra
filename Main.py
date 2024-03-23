#in this file can solve linear systems and can find inverse of matrices
#from AugmentedMatrix import *
from AugmentedMatrix import *

#to solve linear system:
rows = [[2, 3, 1, 2], [1, 4, 5, 6], [1, 6, 3, 5]]
m = AugmentedMatrix(Matrix(rows), False) #False for linear system
m.solve()


"""
#to find inverse of matrix
square = [[2, 7, 1], [1, 4, -1], [1, 3, 0]]
m1 = Matrix(square)


m1Inverse = Matrix.inverse(m1)
m1Inverse.printMatrix()
"""

