import numpy as np

array1=np.array([2,4,5,6,7,8])


np.save('abc.txt.npy',array1)

load_array=np.load('abc.txt.npy')

print(load_array)

