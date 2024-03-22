"""
Row Reduction Algorithm on Augmented Matrix:
1. To solve linear systems
2. To find inverse of matrix
algorithm for solving system of linear equations or finding a matrix's inverse using RREF assuming the following:
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

AugmentedMatrix represents the coefficient matrix and the constant matrix
For linear systems, constant matrix has 1 col
For finding inverse of a matrix, constant matrix is identity matrix I: nxn and coefficient matrix is nxn as well

For system of linear equations:
example: 2x -3y = 5 will be turned into 
    r = [2, -3 ,5]
    len(r) - 1  = number of variables 
    len(r) = num columns

same reasoning for finding inverse of matrix by using Augmented matrix [A I]

"""    
from Matrix import *
class AugmentedMatrix:
    # takes Matrix m as param to use m.rows
    # 2D list: list of rows (or list of ri where ri is list of coefficients)
    # [r1, r2, .., rn]
    # len(rows) = number of equations in system   
    # rows represents augmented matrix
    def __init__(self, matrix):
        if not isinstance(matrix, Matrix):
            raise Exception("AugmentedMatrix takes Matrix as input")
        self.matrix = matrix
        self.rows = matrix.rows
        self.numEquations = len(self.rows)
        self.numVars = len(self.rows[0])-1
        
        
        
    #def getConstantMatrix(self):
        #constant matrix is last column (rightmost column) of 2D grid
     #   return [row[len(row)-1] for row in self.rows]

    #ELEMENTARY ROW OPERATIONS ON AUGMENTED MATRIX: 
    def swapRows(self, i, j):
        #modifies self.rows
        #print("swapping row "+str(i)+" and "+str(j))
        temp = [c for c in self.rows[i]]
        for x in range(len(self.rows[i])):
            self.rows[i][x] = self.rows[j][x]
            self.rows[j][x] = temp[x]
    
    def multiplyRow(self, r, s):
        if s==0:
            raise Exception("cannot multiply row by 0")
        #multiplies every entry of self.rows[r] by s
        #print("multiplying row "+str(r)+" by "+str(s))
        for i in range(len(self.rows[r])):
            self.rows[r][i] *= s
    
    def addRows(self, r1, r2, c):
        # r1 += c * r2, self.rows[r1] is changed
        #print("adding "+str(c)+" * row "+str(r2)+" into row "+str(r1))
        for i in range(len(self.rows[r1])):
            self.rows[r1][i] += c*self.rows[r2][i]
    
    
    def solve(self, inverseOrSystem):
        # inverseOrSystem = True if this AugmentedMatrix is used to find inverse of matrix, self of form [ A I ]
        # inverseOrSystem = False if this AugmentedMatrix is used to solve linear system, self of form [ A b ]
        # perform RR (row reduction) algorithm on augmented matrix
        # solution is the constant matrix of the augmented matrix once the RR algorithm terminates 
        #print("performing row reduction to augmented matrix...")
        currentRow = 0
        while currentRow<len(self.rows):
            self.roundAllEntries()#to get rid of errors due to floats
            #self.matrix.printMatrix() 
            if self.allZeroes(currentRow, 0):
                break
            
                        
            #print(currentRow)
            row, col = self.getRowWithFirstNonZeroEntry(currentRow)
            
            if currentRow!=row:
                self.swapRows(currentRow, row) # move row to top position
            self.multiplyRow(currentRow, 1/self.rows[currentRow][col]) # set val to 1 by mutiplying val by 1/val (create leading 1)
            for r in range(len(self.rows)):#subtract multiples of row with leading 1 from rows below it to make entries below leading 1 equal to 0
                if r!= currentRow:
                    self.addRows(r, currentRow, -self.rows[r][col])
            
            currentRow+=1
        #self.matrix.printMatrix() #done with row reduction algo, self.rows is in RREF
        if not inverseOrSystem:
            if self.checkInconsistent():
                print("System is inconsistent. There are no solutions")
            else:
                print("System is consistent.")
                if self.hasOneSolution():
                    print("System has 1 solution")
                    #constantMatrix = self.getConstantMatrix()
                    for i in range(self.numVars):
                        print("x"+str(i+1)+" = "+str(self.rows[i][self.numVars]))
                else:
                    print("System has infinitely many solutions")
                    #either a row has a leading one or it is a row entirely of zeroes
                    #find number of leading variables, assign non leading variables as parameters and solve for leading variables in terms of parameters
                    for row in self.rows:
                        leadingOne = self.findLeadingOne(row)
                        if leadingOne is not None:
                            const="" if row[self.numVars]==0 else str(row[self.numVars])
                            s="x"+str(leadingOne+1)+" ="
                            rhs=const
                            for d in range(leadingOne+1, len(row)-1):
                                if row[d]!=0:
                                    cf=str(-row[d])
                                    if row[d]<0:
                                        cf="+"+cf
                                    rhs+=" "+cf+"*x"+str(d+1)
                            if rhs=="":
                               rhs = " 0.0"
                            print(s+rhs)
                        else:
                            break #if row is zero then return, all rows below that one will be zero as well
            print("Linear System solved")    

    def findLeadingOne(self, row):
        #return index of leading 1 in row, return None if no leading 1 (row of all zeroes)
        for c in range(len(row)):
            if row[c]==1:
                return c
        return None

    def hasOneSolution(self):
        #assumes system is consistent
        #numVars = len(self.rows[0])-1
        #numEquations = len(self.rows)
        if self.numEquations<self.numVars:
            return False
        #system has 1 solution when the coefficient matrix (up until row numVars) is equal to the identity matrix
        for r in range(self.numVars):
            for c in range(self.numVars):
                if r==c and self.rows[r][c]!=1:
                    return False
                elif r!=c and self.rows[r][c]!=0:
                    return False
        return True
    
    def checkInconsistent(self):
        #system is inconsistent when the last row of self.rows = [0,0,0...1]
        v = [0] * (self.numVars)
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
