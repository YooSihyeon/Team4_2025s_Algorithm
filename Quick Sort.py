def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
if __name__ == "__main__":
    n = int(input()) #시험에서 n+리스트, 2줄이라면 쓰고 그게 아니면 빼기  
    numbers = list(map(int, input().split()))
    print(*quick_sort(numbers))  # 각 정렬 알고리즘에 맞게 함수명 바꾸기

# 퀵 정렬 (Quick Sort)
# 시간복잡도: O(n log n) - 평균, O(n^2) - 최악 (pivot이 한쪽에 치우친 경우)
# 공간복잡도: O(log n) - 평균 (재귀 호출 스택)
# 특징: 분할 정복. 매우 빠름. 불안정 정렬.

# 입력 예시:
# 7 2 5 1 4
# 출력 예시:
# 1 2 4 5 7
# 리스트만 주어질 경우에는 n = int(input()) 부분 생략
