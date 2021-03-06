import numpy as np
import random

n = int(input("2부터 6까지의 숫자 중 하나를 입력하세요: "))  #숫자 입력받음

ar = np.random.randint(10, size=(n, n))  #1부터 10까지 랜덤으로 cost를 가지는 행렬 생성 및 출력
array = ar + 1
print(array)

answer = []  #최종 답 리스트
cost=100000   #초기 값을 매우 크게 설정
c=0  #while문을 10만번 돌리기 위해 필요한 변수
while c<=100000:  #10만번 반복
    a=[i for i in range(n)]   #0부터 n-1까지 리스트 2개 생성
    b=[i for i in range(n)]
    li=[]                       #뽑은 값의 위치를 저장할 곳
    cal=0                          #뽑은 값들의 cost를 계산
    c+=1
    for i in range(n):              #n*n 행렬이므로 5개 뽑음
        x=random.sample(a,1)[0]
        y=random.sample(b,1)[0]
        li.append([x,y])            #뽑은 값들을 저장
        a.remove(x)
        b.remove(y)
        cal +=array[x][y]           # 그 값들의 cost를 합하여 계산
    if cost>cal:                    # 뽑은 값들의 cost인 cal이 기존의 cost보다 작으면 대체
        cost = cal                     #또한, 최종 리스트 값도 대체
        answer=li

print(cost)
print(answer)                       # 결과값은 비용의 합과 그때의 기계별 비용을 (행,열)로 나타냄

import pandas as pd

arr = np.array(answer)
df = pd.DataFrame(arr)

df.to_csv('team13_groupworkoutputresult.csv', index=False)      #csv에서 결과값은 2번째 줄부터 기계별 비용을 (행,열)로 나타냄
