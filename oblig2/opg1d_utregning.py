import numpy as np
from sympy import *


A = np.array([[1,2,4,8],
            [1,3,9,27],
            [1,4,16,64],
            [1,5,25,125],
            [1,6,36,216]])
AT = A.transpose()
b = np.array([[7],
             [3],
             [5],
             [4],
             [3]])
ATA = AT@A
ATb = AT@b

likn = np.column_stack((ATA, ATb))
los = Matrix(likn).rref()

print(f'A:\n{A}')
print(f'AT:\n{AT}')
print(f'b:\n{b}')
print(f'ATA:\n{ATA}')
print(f'ATb:\n{ATb}')
print(f'likning:\n{likn}')
print(f'ATb:\n{los}')
  