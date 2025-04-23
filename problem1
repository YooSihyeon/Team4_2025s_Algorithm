def insertion_sort(n, arr):
    n = len(arr)
    # 두 번째 원소부터 시작해서 앞의 정렬된 부분과 비교하며 삽입
    for i in range(1, len(arr)):
        key = arr[i]        # 현재 삽입하려는 값
        j = i - 1
        # key보다 큰 값들을 한 칸씩 뒤로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # key를 알맞은 위치에 삽입
        arr[j + 1] = key
    return arr


    # 예시 입력
ex = [7, 2, 5, 1, 4]

insertion_sort(5, ex)