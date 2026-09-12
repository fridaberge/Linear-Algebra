from sympy import *

M = Matrix([[1,2,4,8,7],[1,3,8,27,3],[1,4,16,64,5],[1,5,25,125,4],[1,6,36,216,3]])
M_rref = M.rref()
print("\nThe Row echelon form of matrix M and the pivot columns :", M_rref)