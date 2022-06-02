#import pandas as pd


#랜덤 행렬 생성 위해 numpy 모듈 import
import numpy as np

#n*n 행렬 랜덤 생성 위한 n값 입력 부분
n = int(input('2 이상 6 이하의 정수 n을 입력하세요: '))

'''
ar = np.random.randint(10, size=(n,n))
array = ar+1
'''

#1 이상 11 미만의 instance 값 가지는 n*n 행렬 생성 및 print
import random
array = np.random.randint(low=1, high=11, size=(n,n))
print(array)