# importing the required module 
import matplotlib.pyplot as plt
import numpy as np

def q(t):
    return 129-(135*t)+(52*(t**2))-((17/2)*(t**3))+((1/2)*(t**4))
# def p(t):
#     return (177/5)-((173/7)*t)+((87/14)*(t**2))-((1/2)*(t**3))


x = [2,3,4,5,6]
y = [7,3,5,4,3]
t = np.linspace(1.9, 6.1)

plt.scatter(x,y, marker='o', color='red', s=7) 
plt.plot(t, q(t), color='orange',label='q(t)')
# plt.plot(t, p(t), color='blue', label='p(t)')
plt.xlim(1.9, 6.1)
plt.xlabel('t - axis') 
plt.ylabel('s - axis') 
  
plt.title('q(t) og punkt 1-5') 
plt.savefig("opg1f.png");