#3번 문제 - 숫자 등장 횟수(빈도수) 정렬

# 리스트 요소의 빈도수를 쉽게 셀 수 있는 Counter 클래스 불러오기
from collections import Counter

n = int(input())  # 숫자의 개수 입력 받기 (예: 5)
numbers = list(map(int, input().split()))  # 공백으로 구분된 숫자들을 입력받아 정수 리스트로 변환

counter = Counter(numbers)  # Counter 객체 생성: 각 숫자가 몇 번 나왔는지 세어줌 
# 예: numbers가 [3, 1, 3, 2, 1]이면 -> Counter({3: 2, 1: 2, 2: 1})

sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[1]))
# counter.items()는 (숫자, 빈도수)의 리스트를 반환
# 정렬 기준:
# 1순위: 빈도수 내림차순 (-x[1])
# 2순위: 빈도수 같을 경우, 빈도수 내림차순 (x[1])  

for item in sorted_items:
    print(item)  # (숫자, 빈도수) 형태로 출력. 예: (3, 2), (1, 2), (2, 1)

