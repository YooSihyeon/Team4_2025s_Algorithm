
from collections import Counter

# 입력
n = int(input())
nums = list(map(int, input().split()))

# 등장 횟수 세기
count = Counter(nums)

# 정렬: 등장 횟수 내림차순, 숫자 오름차순
sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))

# 출력
for num, freq in sorted_items:
    print(num, freq)