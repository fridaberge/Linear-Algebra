# importing the required module 
import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np
from numpy import cos, sin, pi
from scipy import integrate

def integrad0(x):
    return (1/2)*x

def integradA(x,n):
    return x*cos(n*x*pi)

def integradB(x,n):
    return x*sin(n*x*pi)

sum0 = quad(integrad0,-1,1)[0]
sumA_4 = 0
sumB_4 = 0
sumA_6 = 0
sumB_6 = 0

X = np.linspace(-2,2, 100)
i = 1
while i<=4:
    sumA_4 += quad(integradA, -1,1,i)[0]*cos(i*pi*X)
    sumB_4 += quad(integradB, -1,1,i)[0]*sin(i*pi*X)
    sumA_6 += quad(integradA, -1,1,i)[0]*cos(i*pi*X)
    sumB_6 += quad(integradB, -1,1,i)[0]*sin(i*pi*X)
    i +=1
while i <= 6:
    sumA_6 += quad(integradA, -1,1,i)[0]*cos(i*pi*X)
    sumB_6 += quad(integradB, -1,1,i)[0]*sin(i*pi*X)
    i+=1

def proj_4(X):
    return sum0+sumA_4+sumB_4

def proj_6(X):
    return sum0+sumA_6+sumB_6

def f(X):
    return X

plt.plot(X, proj_4(X), color='green', label='N=4')
plt.plot(X, proj_6(X), label='N=6')
plt.plot(X, f(X), label='f')


plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
  
plt.title('f(x), proj_4 og proj_6') 
plt.savefig("opg2h.png");

