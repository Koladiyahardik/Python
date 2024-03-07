import numpy as np

#1D Array
ar1=[1,2,3,4,5]
y=np.array(ar1)
print(y)
print(y.ndim)

#2D Array
ar2=[1,2,3,4,5]
y=np.array(ar2,ndmin=2)
print(y)
print(y.ndim)

#3D Array
ar3=[1,2,3,4,5]
y=np.array(ar3,ndmin=3)
print(y)
print(y.ndim)

#nD Array
arn=[1,2,3,4,5]
y=np.array(arn,ndmin=10)
print(y)
print(y.ndim)

#0' Array
y=np.zeros(4)
print(y)

#1' Array
y=np.ones(4)
print(y)

#Empty Array
y=np.empty(4)
print(y)

# Range
y=np.arange(1,10,2)
print(y)
