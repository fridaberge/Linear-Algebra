# importing the required module 
import matplotlib.pyplot as plt
import numpy as np

def p(t):
    return (177/5)-((173/7)*t)+((87/14)*(t**2))-((1/2)*(t**3))

x = [2,3,4,5,6]
y = [7,3,5,4,3]
t = np.linspace(1.9, 6.1, 100)

plt.scatter(x,y, marker='o', color='red', s=7) 
plt.plot(t, p(t))
# plt.xlim(1.9, 6.1)
plt.xlabel('t - axis') 
plt.ylabel('s - axis') 
  
plt.title('p(t) og punkt 1-5') 
plt.savefig("opg1d.png");
# plt.show() 