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

#TODO DO LINEAR TRANSFORMATIONS NEXT AND MAYBE USE PYTHON LIBRARY TO GRAPH VECTORS
#vector is matrix with all rows having size 1 (1 column)
# matrix algebra
#A = Matrix([[2, 1], [-1, 4]])
#A.printMatrix()
#Matrix.inverse(Matrix.sub(Matrix.transpose(A), Matrix([[2,0],[0,2]]))).printMatrix()
#markov chains!:
P = Matrix([[0.5, 0.25,  0.25], [0, 0.5, 0.25], [0.5, 0.25, 0.5]])
s = Matrix([[1], [0], [0]])

Matrix.multiply(Matrix.power(P, 25), s).printMatrix()


#m3 = Matrix([[2], [3], [4]])

#sumMatrix = Matrix.multiply(m2, m3)
#m2.printMatrix()
#print("*")
#m3.printMatrix()
#print("=")
#sumMatrix.printMatrix()
