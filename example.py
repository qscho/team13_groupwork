"""
import numpy as np
from scipy.optimize import linear_sum_assignment
import random

n=5

ar = np.random.randint(10, size=(n,n))
array = ar+1
print(array)



a,b = linear_sum_assignment(array)
print(array[a,b].sum())

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if i!=j and j!=k and k!=l and i!=k and i!=l and j!=l:
                    #sol = 0
"""
"""
import numpy as np
import random

n = 5

ar = np.random.randint(10, size=(n, n))
array = ar + 1
print(array)
print(array[0][1])
print(array[1][0])
# 알고리즘 설명: greedy 한 방법으로, 어떤 두 대각원소의 합이 그 행과 열을 서로 바꾼 다른 원소의
#  합보다 크면
# 대각행렬의 값을 그 두 원소로 스와프.
# 스와프하는 횟수가 0이 될 때 까지 반복
# 어느 부분에 모순이 있는지 모르겠음
c = False
while c is False:
    d = 0
    for i in range(n):
        for j in range(n):
            if (i != j) and (array[i][i] + array[j][j] > array[i][j] + array[j][i]):
                d += 1
                temp1 = array[i][i]
                array[i][i] = array[j][i]
                array[j][i] = temp1
                temp2 = array[j][j]
                array[j][j] = array[i][j]
                array[i][j] = temp2
    if d == 0:
        c = True

print(c)
print(array)


"""

import numpy as np
import random

n = 5

ar = np.random.randint(10, size=(n, n))
array = ar + 1
print(array)


answer = []
cost=100
c=0
while c<=100000:
    a=[i for i in range(n)]
    b=[i for i in range(n)]
    li=[]
    cal=0
    c+=1
    for i in range(n):
        x=random.sample(a,1)[0]
        y=random.sample(b,1)[0]
        li.append([x,y])
        a.remove(x)
        b.remove(y)
        cal +=array[x][y]
    if cost>cal:
        cost = cal
        answer=li

print(cost)
print(answer)

