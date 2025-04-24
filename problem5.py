# 1000000개의 랜덤 숫자 리스트 생성
import random
import time

arr = random.sample(range(1, 1000001), 1000000)
start = time.time()
result = sorted(arr)
end = time.time() 
spand_time=end-start
print(f'{result[:10]}')
print(f'실행 시간 :{spand_time:.4f}')
if spand_time>=3:
    print('PASSCORD = \'False\'')
else:
    print('PASSCORD = \'TRUE\'')

# 출력 결과
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#실행 시간 :0.3798
#PASSCORD = 'TRUE'