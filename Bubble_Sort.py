def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
if __name__ == "__main__":
    n = int(input()) #시험에서 n+리스트, 2줄이라면 쓰고 그게 아니면 빼기  
    numbers = list(map(int, input().split()))
    print(*bubble_sort(numbers))  # 각 정렬 알고리즘에 맞게 함수명 바꾸기

# 버블 정렬 (Bubble Sort)
# 시간복잡도: O(n^2) - 최악/평균
# 공간복잡도: O(1)
# 특징: 단순하고 구현이 쉬움, 하지만 느림

# 입력 예시:
# 7 2 5 1 4
# 출력 예시:
# 1 2 4 5 7
# 리스트만 주어질 경우에는 n = int(input()) 부분 생략

