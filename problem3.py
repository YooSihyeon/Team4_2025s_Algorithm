#3번 문제 - 숫자 등장 횟수(빈도수) 정렬

from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))

counter = Counter(numbers)
sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[1]))

for item in sorted_items:
    print(item)  # (숫자, 빈도수) 튜플 형태
