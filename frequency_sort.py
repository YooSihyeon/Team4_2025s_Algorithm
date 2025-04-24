#3번 문제 - 숫자 등장 횟수(빈도수) 정렬

from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))

counter = Counter(numbers)
sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

for num, count in sorted_items:
    print(num, count)
