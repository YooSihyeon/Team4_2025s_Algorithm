# 1000000개의 랜덤 숫자 리스트 생성
import random
import time

arr = random.sample(range(1, 1000001), 100)
start = time.time()
result = arr.sort()
end = time.time() 
print(f"{result}: {end - start:.4f} sec")


# 출력 결과
'''
hello
test try
[1, 2, 4, 5, 7]
'''