"""algorithm for solving system of linear equations using RREF assuming the following:
    A system (matrix) is represented as a list of rows:
    __    __
    |  R1  |
    |  R2  |
    |  R3  |
..
    |  RN  |
    |_    __

1 row is 1 equation in a system of linear equations
1 row represented as list of coefficients (left+right of equal sign)
example: 2x -3y = 5 will be turned into 
    r = [2, -3 ,5]
    len(r) - 1  = number of variables 
    len(r) = num columns
"""    
class AugmentedMatrix:
    # 2D list: list of rows (or list of ri where ri is list of coefficients)
    # [r1, r2, .., rn]
    # len(rows) = number of equations in system   
    # rows represents augmented matrix
    def __init__(self, rows):
        self.numEquations = len(rows)
        self.numVariables = len(rows[0])-1
        self.rows = rows
        if not self.isValid():
            raise Exception("not a valid matrix, must input a 2d grid represented as list of list of numbers")
        
    
    def isValid(self):
        #checks wheter or not self.rows is a rectangular 2d array (each row must have the same number of columns)
        for i in range(1,len(self.rows)):
            if len(self.rows[i])!=len(self.rows[0]):
                return False
        return True
        
    def solve(self):
        # perform RR (row reduction) algorithm on augmented matrix and return solution
        # solution is the constant matrix of the augmented matrix once the RR algorithm terminates 
        # sol is of the form: [s1, s2, .., sn]
        print("performing row reduction to augmented matrix...")
        while not self.rows.isRowReduced():
            print(self.rows)
            #TODO iteratively modify self.rows until it is row reduced
        return getConstantMatrix()      
    
    def isRowReduced(self):
        #TODO
        return False

    def getConstantMatrix(self):
        #constant matrix is last column (rightmost column) of 2D grid
        return [row[len(row)-1] for row in self.rows]



rows = [[2, -3, 5],[1, 2, -4]]
m1 = AugmentedMatrix(rows)


#m1.solve()
print(m1.getConstantMatrix())
