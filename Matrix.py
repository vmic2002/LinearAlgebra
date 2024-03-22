#Matrix.py for regular matrices, not augmented matrix
import AugmentedMatrix
class Matrix:
    #2D array where each row must have same length (must be rectangular)
    def __init__(self, rows):
        self.rows = rows
        if not self.isValid():
            raise Exception("not a valid matrix, must input a 2d grid represented as list of list of numbers")
        self.numRows = len(rows)
        self.numCols = len(rows[0])    
   
    
    def add(m1, m2):
        #TODO IMPLEMENT
        # RETURN NEW MATRIX THAT IS SUM OF m1 AND m2
        if not isinstance(m1, Matrix) or not isinstance(m2, Matrix):
            raise Exception("Matrix.add takes Matrix, Matrix as param")
        print("adding matrices")
        
    def sub(m1, m2):
        #TODO implememnt
        # return new matrix that is m1-m2
        print("substracting two matrices")
        if not isinstance(m1, Matrix) or not isinstance(m2, Matrix):
            raise Exception("Matrix.sub takes Matrix, Matrix as param") 
    

    def multiply(m1, m2):
        #TODO 
        # return new matrix m1*m2
        print("multiplying two matrices")
        if not isinstance(m1, Matrix) or not isinstance(m2, Matrix):
            raise Exception("Matrix.multiply takes Matrix, Matrix as param")

    def transpose(m):
        #TODO
        # return new matrix transpose of m
        if not isinstance(m, Matrix):
            raise Exception("Matrix.transpose takes Matrix as param")

    def inverse(M):
        # return new Matrix() that is inverse of M
        # to find inverse, create AugmentedMatrix = [ M I ]
        # then call solve func of AugmentedMatrix
        if not isinstance(M, Matrix):
            raise Exception("Matrix.inverse takes Matrix as param")
        rows = []
        for r in range(M.numRows):
            newRow = []
            for c in range(M.numCols):
                newRow.append(M.rows[r][c])
            for c in range(M.numCols, 2*M.numCols):
                newRow.append((1 if r==(c-M.numCols) else 0))
            rows.append(newRow)
        newMatrix = Matrix(rows)#newMatrix is [M I]
        augmentedMatrix = AugmentedMatrix.AugmentedMatrix(newMatrix)
        augmentedMatrix.solve(True) #after solve(), augmentedMatrix is [I inverse(M)]
        #print("augmented matrix inverse")
        #augmentedMatrix.matrix.printMatrix()
        inverseMatrix = []
        for r in range(M.numRows):
            newRow = []
            for c in range(M.numCols, 2*M.numCols):
                newRow.append(augmentedMatrix.rows[r][c])
            inverseMatrix.append(newRow)    
        return Matrix(inverseMatrix)


    def isValid(self):
        #checks wheter or not self.rows is a rectangular 2d array (each row must have the same number of columns)
        for i in range(1,len(self.rows)):
            if len(self.rows[i])!=len(self.rows[0]):
                return False
        return True
    
    def printMatrix(self):
        print("--------------------")
        for row in self.rows:
            print(row)
        print("--------------------")    
