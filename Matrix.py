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
   
    
    def sum(m1, m2):
        # RETURN NEW MATRIX THAT IS SUM OF m1 AND m2
        if not isinstance(m1, Matrix) or not isinstance(m2, Matrix):
            raise Exception("Matrix.sum takes Matrix, Matrix as param")
        if not Matrix.sameDimensions(m1, m2):
            raise Exception("Matrix.sum takes matrices of same dimensions")
        rows = []
        for r in range(m1.numRows):
            newRow = []
            for c in range(m1.numCols):
                 newRow.append(m1.rows[r][c]+m2.rows[r][c])
            rows.append(newRow)
        return Matrix(rows)
        
    def sub(m1, m2):
        # return new matrix that is m1-m2
        if not isinstance(m1, Matrix) or not isinstance(m2, Matrix):
            raise Exception("Matrix.sub takes Matrix, Matrix as param")
        if not Matrix.sameDimensions(m1, m2):
            raise Exception("Matrix.sub takes matrices of same dimensions")
        rows = []
        for r in range(m1.numRows):
            newRow = []
            for c in range(m1.numCols):
                newRow.append(m1.rows[r][c]-m2.rows[r][c])
            rows.append(newRow)
        return Matrix(rows)  
 
    def multiply(m1, m2):
        # return new matrix m1*m2
        if not isinstance(m1, Matrix) or not isinstance(m2, Matrix):
            raise Exception("Matrix.multiply takes Matrix, Matrix as param")
        if not m1.numCols == m2.numRows:
            raise Exception("Matrix.multiply takes matrices of correct dimensions for multiplication to be defined")
        rows = []
        for r in range(m1.numRows):
            newRow = []
            for c1 in range(m2.numCols):#c1 is to loop trhough m2 cols
                dotProduct = 0
                for c in range(m1.numCols):
                    dotProduct += m1.rows[r][c]*m2.rows[c][c1]
                newRow.append(dotProduct)
            
            rows.append(newRow)
        return Matrix(rows)       


 
    def transpose(m):
        #TODO
        # return new matrix transpose of m
        if not isinstance(m, Matrix):
            raise Exception("Matrix.transpose takes Matrix as param")

    def inverse(M):
        # return new Matrix() that is inverse of M
        # to find inverse, create AugmentedMatrix = [ M I ]
        # then call solve func of AugmentedMatrix to get [ I inverse(M) ]
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
        augmentedMatrix = AugmentedMatrix.AugmentedMatrix(newMatrix, True)
        augmentedMatrix.solve() #after solve(), augmentedMatrix is [I inverse(M)]
        #TODO NEED TO CHECK THAT AUGMENTEDMATRIX IS OF FORM [I INVERSE(M)]
        #TODO IF LEFT PART IS NOT I, THEN THE MATRIX M IS NOT INVERTIBLE AND SHOULD RAISE EXCEPTION
        #TODO IF LEFT PART IS I, THEN RIGHT PART WILL BE INVERSE(M) so M is invertible
        inverseMatrix = []
        for r in range(M.numRows):
            newRow = []
            for c in range(M.numCols, 2*M.numCols):
                newRow.append(augmentedMatrix.rows[r][c])
            inverseMatrix.append(newRow)    
        return Matrix(inverseMatrix)

    def sameDimensions(m1, m2):
        if not isinstance(m1, Matrix) or not isinstance(m2, Matrix):
            raise Exception("Matrix.sameDimensions takes two Matrices as input")
        return m1.numRows == m2.numRows and m1.numCols == m2.numCols

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
