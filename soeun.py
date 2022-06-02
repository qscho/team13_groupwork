#랜덤 행렬 생성 위해 numpy 모듈 import
import numpy as np

#n*n 행렬 랜덤 생성 위한 n값 입력 부분
n = int(input('2 이상 6 이하의 정수 n을 입력하세요: '))

#1 이상 11 미만의 instance 값 가지는 n*n 행렬 생성 및 print
import random
array = np.random.randint(low=1, high=11, size=(n,n))

'''
ar = np.random.randint(10, size=(n,n))
array = ar+1
'''
print(array)


#솔루션을 csv 파일로 출력하여 저장
 #1
import pandas as pd
result_assigned = [저장,할,리스트,데이터]
df = pd.DataFrame(result_assigned, columns = ['cost'])
print(df)

df.to_csv("team13_groupwork\output\result.csv", index=False)


 #2
import pandas as pd
result_assigned = [저장,할,리스트,데이터]
df = pd.DataFrame(result_assigned)
df.to_csv("team13_groupwork\output\result.csv", header=False, index=False)

print(df)



#로그 관리 및 예외 처리_데이터 생성/솔루션 도출 동작 script에 log로 출력
'''
import logging

logger = logging.getLogger("main")
stream_hander = logging.StreamHandler()
logger.addHandler(stream_hander)

logger.setLevel(logging.DEBUG)
logger.debug("틀렸잖아")
logger.info("확인해")
logger.warning("조심해")
logger.error("에러 났어")
logger.critical("망...")
'''