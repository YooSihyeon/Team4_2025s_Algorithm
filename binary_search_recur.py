# 재귀형 이진 탐색
# 입력: 정수 개수 N, 정렬된 리스트, 찾을 값
# 출력: YES / NO

def binary_search_recur(arr, target, left, right):
    if left > right:
        return "NO"
    mid = (left + right) // 2
    if arr[mid] == target:
        return "YES"
    elif arr[mid] < target:
        return binary_search_recur(arr, target, mid + 1, right)
    else:
        return binary_search_recur(arr, target, left, mid - 1)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    target = int(input())
    print(binary_search_recur(arr, target, 0, n - 1))

# 예시:
# 7
# 1 3 5 7 9 11 13
# 5
# 출력: YES
