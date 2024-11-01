import numpy as np

iter = np.fromiter((a for a in range (1,20) if a%2==0), int)
print (iter)


filterr = iter > 10

iter = iter[filterr]

print(iter)

