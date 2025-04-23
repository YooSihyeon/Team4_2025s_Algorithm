# 반복형 이진 탐색
# 입력: 정수 개수 N, 정렬된 리스트, 찾을 값
# 출력: YES / NO

def binary_search_iter(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return "YES"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "NO"

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    print(binary_search_iter(arr, target))

# 예시 입력:
# 7
# 1 3 5 7 9 11 13
# 5
# 출력: YES
