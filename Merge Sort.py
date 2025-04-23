def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
if __name__ == "__main__":
    n = int(input()) #시험에서 n+리스트, 2줄이라면 쓰고 그게 아니면 빼기  
    numbers = list(map(int, input().split()))
    print(*merge_sort(numbers))  # 각 정렬 알고리즘에 맞게 함수명 바꾸기

# 병합 정렬 (Merge Sort)
# 시간복잡도: O(n log n) - 모든 경우
# 공간복잡도: O(n)
# 특징: 분할 정복. 안정 정렬. 추가 메모리 필요.

# 입력 예시:
# 7 2 5 1 4
# 출력 예시:
# 1 2 4 5 7
# 리스트만 주어질 경우에는 n = int(input()) 부분 생략
