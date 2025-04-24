# 1000000개의 랜덤 숫자 리스트 생성
import random
import time

arr = random.sample(range(1, 1000001), 1000000)
start = time.time()
result = sorted(arr)
end = time.time() 
spand_time=end-start
print(f'실행 시간 :{spand_time:.4f}')
print(f'출력 결과: {result[:10]}')

if spand_time>=3:
    print('False')
else:
    print('True')

# 출력 결과
'''
hello
test try
[1, 2, 4, 5, 7]
'''