# 1000000개의 랜덤 숫자 리스트 생성
import random
import time

arr = random.sample(range(1, 1000001), 1000000) # 1부터 1000000까지 중에서 겹치지 않게 1000000개의 숫자를 뽑아서 리스트로 만듬
start = time.time() # 시작 시간 측정
result = sorted(arr) # 리스트 정렬 
end = time.time() # 종료 시간 측정 
spand_time=end-start # 걸린 시간 계산 
print(f'{result[:10]}') # 정렬된 리스트에서 10개만 표시 
print(f'실행 시간 :{spand_time:.4f}') # 걸린 시간 표시(소수점 아래 4자리까지)
if spand_time>=3: # 정렬에 걸린 시간이 3초 이상일 경우 FALSE 출력 
    print('PASSCORD = \'False\'')
else: # 정렬에 걸린 시간이 3초 이내인 경우(조건 만족): TRUE 출력 
    print('PASSCORD = \'TRUE\'') 

# 출력 결과
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#실행 시간 :0.3798
#PASSCORD = 'TRUE'

"""
프롬프트 내역
1. 1~100까지의 값을 랜덤으로 추출해서 리스트 만들건데 겹치지 않게 하고 싶으면 어떡해?
2.dfs 코드 내에서 0에 도달하는 문제를 풀고 있는데 가능한 모든 경우의 수를 출력하려면 어떡해야 해? 한 번에서 그치거든 지금은
"""