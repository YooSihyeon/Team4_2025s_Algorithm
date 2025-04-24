print('hello')
print('test try')

def selection_sort(n, arr):
    n = len(arr)
    # 리스트의 앞에서부터 차례대로 최소값을 선택해 정렬
    for i in range(n):
        min_idx = i  # 현재 위치를 최소값이라고 가정
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # 더 작은 값이 있으면 해당 인덱스로 갱신
        # 최소값을 현재 위치로 교환
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
# 예시 입력
ex = [7, 2, 5, 1, 4]

a=selection_sort(5, ex) # 리스트 정렬 함수
print(a) # 결과 출력

# 출력 결과
'''
hello
test try
[1, 2, 4, 5, 7]
'''