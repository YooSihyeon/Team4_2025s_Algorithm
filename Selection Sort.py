def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
if __name__ == "__main__":
    n = int(input()) #시험에서 n+리스트, 2줄이라면 쓰고 그게 아니면 빼기  
    numbers = list(map(int, input().split()))
    print(*selection_sort(numbers))  # 각 정렬 알고리즘에 맞게 함수명 바꾸기

# 선택 정렬 (Selection Sort)
# 시간복잡도: O(n^2) - 모든 경우 동일
# 공간복잡도: O(1)
# 특징: 가장 작은 값을 선택해서 앞쪽에 위치시킴. 안정 정렬이 아님.

# 입력 예시:
# 7 2 5 1 4
# 출력 예시:
# 1 2 4 5 7
# 리스트만 주어질 경우에는 n = int(input()) 부분 생략
