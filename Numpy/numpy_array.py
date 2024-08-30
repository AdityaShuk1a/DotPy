import numpy as np

a = np.full(5,3)
b = np.full(6,5)
filter_arr = a %2==0
b= b.reshape(2,3)
print(a)
print(b)
print(b.base)
print(a[filter_arr])
c = np.fromiter((d for d in range(10) if d%2==0  ), int)
print(c)