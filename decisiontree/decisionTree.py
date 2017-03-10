import numpy as np
from sklearn import random_projection
print("adf")
a = np.array([[10, 0], [0, 10]])
print(a)
print(a * a)
print(a *2)
print(a + a)
b = np.matrix(a)
print(b)
print(b*b)
print(a*b)
rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')
print(X.dtype)

transformer = random_projection.GaussianRandomProjection()
#X_new =  transformer.f

c = np.array([1, 2, 3,4])
c
print(c.transpose())
print(c)


