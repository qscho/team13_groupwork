import numpy as np
from scipy.optimize import linear_sum_assignment
import random

n=5

ar = np.random.randint(10, size=(n,n))
array = ar+1
print(array)



a,b = linear_sum_assignment(array)
print(array[a,b].sum())

"""
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if i!=j and j!=k and k!=l and i!=k and i!=l and j!=l:
                    #sol = 0
"""