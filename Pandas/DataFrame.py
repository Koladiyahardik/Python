import matplotlib.pyplot as plt
import numpy as np

x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2,1,1)
plt.bar(x,y)

x=np.array([0,1,2,3])
y=np.array([59,25,30,40])
plt.subplot(2,2,1)
plt.scatter(x,y)

x=np.array([0,1,2,3])
y=np.array([5,6,70,80])
plt.subplot(2,1,2)
plt.scatter(x,y)

x=np.array([0,1,2,3])
y=np.array([90,100,80,79])
plt.subplot(2,2,2)
plt.bar(x,y)
plt.show()
plt.show()




