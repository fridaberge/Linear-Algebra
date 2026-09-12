import numpy as np
from sympy import *

M = np.array([[1,2,4,8,16,7],
            [1,3,9,27,81,3],
            [1,4,16,64,256,5],
            [1,5,25,125,625,4],
            [1,6,36,216,1296,3]])
los = Matrix(M).rref()
print("\nThe Row echelon form of matrix M and the pivot columns :", los)