# LinearAlgebra
Python program to perform various matrix operations and elementary row reduction.

1. Solving Linear System of Equations:
```python
rows = [[2, 3, 1, 2], [1, 4, 5, 6], [1, 6, 3, 5]]
m = AugmentedMatrix(Matrix(rows), False) #False for linear system
m.solve()
```

2. Finding Inverses of Matrices:
```python
square = [[2, 7, 1], [1, 4, -1], [1, 3, 0]]
m1 = Matrix(square)
m1Inverse = Matrix.inverse(m1)
m1Inverse.printMatrix()
```

3. Matrix Algebra:
```python
A = Matrix([[2, 1], [-1, 4]])
A.printMatrix()
Matrix.inverse(Matrix.sub(Matrix.transpose(A), Matrix([[2,0],[0,2]]))).printMatrix()
```

4. Markov Chains:
```python
P = Matrix([[0.5, 0.25,  0.25], [0, 0.5, 0.25], [0.5, 0.25, 0.5]])
s = Matrix([[1], [0], [0]])
Matrix.multiply(Matrix.power(P, 25), s).printMatrix()
```



All Matrix functions:
```python
  def sum(m1, m2):
  def sub(m1, m2):
  def multiply(m1, m2):
  def power(m, e):
  def transpose(m):
  def inverse(m):
  def sameDimensions(m1, m2):
  def isValid(self):
  def printMatrix(self):
```
