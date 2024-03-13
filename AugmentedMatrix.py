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
        
    def getConstantMatrix(self):
        #constant matrix is last column (rightmost column) of 2D grid
        return [row[len(row)-1] for row in self.rows]

    #ELEMENTARY ROW OPERATIONS ON AUGMENTED MATRIX: 
    def swapRows(self, i, j):
        #modifies self.rows
        print("swapping row "+str(i)+" and "+str(j))
        temp = [c for c in self.rows[i]]
        for x in range(len(self.rows[i])):
            self.rows[i][x] = self.rows[j][x]
            self.rows[j][x] = temp[x]
    
    def multiplyRow(self, r, s):
        if s==0:
            raise Exception("cannot multiply row by 0")
        #multiplies every entry of self.rows[r] by s
        print("multiplying row "+str(r)+" by "+str(s))
        for i in range(len(self.rows[r])):
            self.rows[r][i] *= s
    
    def addRows(self, r1, r2, c):
        # r1 += c * r2, self.rows[r1] is changed
        print("adding "+str(c)+" * row "+str(r2)+" into row "+str(r1))
        for i in range(len(self.rows[r1])):
            self.rows[r1][i] += c*self.rows[r2][i]
    
    def printMatrix(self):
        print("--------------------")
        for row in self.rows:
            print(row)
        print("--------------------")
    
    
    def solve(self):
        # perform RR (row reduction) algorithm on augmented matrix and return solution
        # solution is the constant matrix of the augmented matrix once the RR algorithm terminates 
        # sol is of the form: [s1, s2, .., sn]
        print("performing row reduction to augmented matrix...")
        currentRow = 0
        while currentRow<len(self.rows):
            self.roundAllEntries()#to get rid of errors due to floats
            self.printMatrix() 
            if self.allZeroes(currentRow, 0):
                return self.getConstantMatrix()
            
                        
            #print(currentRow)
            row, col = self.getRowWithFirstNonZeroEntry(currentRow)
            
            if currentRow!=row:
                self.swapRows(currentRow, row) # move row to top position
            self.multiplyRow(currentRow, 1/self.rows[currentRow][col]) # set val to 1 by mutiplying val by 1/val (create leading 1)
            for r in range(len(self.rows)):#subtract multiples of row with leading 1 from rows below it to make entries below leading 1 equal to 0
                if r!= currentRow:
                    self.addRows(r, currentRow, -self.rows[r][col])
            
            currentRow+=1
        #done with row reduction algo, self.rows is in RREF
        if self.checkInconsistent():
            print("System is inconsistent. There are no solutions")
        else:
            print("System is consistent.")
            if self.hasOneSolution():
                print("System has 1 solution")
                #TODO find number of leading variables, assign non leading variables as parameters and solve for leading variables in terms of parameters
            else:
                print("System has infinitely many solutions")
        return self.getConstantMatrix()      


    def hasOneSolution(self):
        #system has 1 solution when the coefficient matrix is equal to the identity matrix
        for r in range(len(self.rows)):
            for c in range(len(self.rows[0])-1):
                if r==c and self.rows[r][c]!=1:
                    return False
                elif r!=c and self.rows[r][c]!=0:
                    return False
        return True
    
    def checkInconsistent(self):
        #system is inconsistent when the last row of self.rows = [0,0,0...1]
        v = [0] * (len(self.rows[0])-1)
        v.append(1) 
        return v==self.rows[len(self.rows)-1]

    def roundAllEntries(self):
        for row in range(len(self.rows)):
            for col in range(len(self.rows[0])):
                self.rows[row][col] = round(self.rows[row][col], 5)
                
    
    def allZeroes(self, startingRow, startingCol):
        for r in range(startingRow, len(self.rows)):
            for c in range(startingCol, len(self.rows[0])):
                if self.rows[r][c]!=0:
                    return False
        return True        


    def getRowWithFirstNonZeroEntry(self, startingRow):
        for col in range(len(self.rows[0])):
            for row in range(startingRow, len(self.rows)):
                if (self.rows[row][col]!=0):
                    return row, col
        raise Exception("should never get here")                     
    

rows = [
        [1, -1, 2, -1, 0],
        [2, 2, 0, 1, 0], 
        [3, 1, 2, -1, 0]]
rows1 = [[1,2,4],[3,6,18]]
rows2 = [[1,1,3], [1,1,2]]
rows3 = [[1,0,0,1],[0,1,0,1],[0,0,1,1]]
#rows = [[2, 3, 4, 7], [1, 4, 5, 8], [5, 4, 3, 5]]
m1 = AugmentedMatrix(rows)


m1.solve()

