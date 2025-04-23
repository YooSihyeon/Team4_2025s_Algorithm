def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
if __name__ == "__main__":
    n = int(input()) #시험에서 n+리스트, 2줄이라면 쓰고 그게 아니면 빼기  
    numbers = list(map(int, input().split()))
    print(*insertion_sort(numbers))  # 각 정렬 알고리즘에 맞게 함수명 바꾸기

# 삽입 정렬 (Insertion Sort)
# 시간복잡도: O(n^2) - 평균/최악, O(n) - 최선 (거의 정렬된 경우)
# 공간복잡도: O(1)
# 특징: 필요할 때만 이동. 소규모 데이터에 적합, 안정 정렬.

# 입력 예시:
# 7 2 5 1 4
# 출력 예시:
# 1 2 4 5 7
# 리스트만 주어질 경우에는 n = int(input()) 부분 생략
