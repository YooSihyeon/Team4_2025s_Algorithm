import random
import time
import numpy as np

# 정렬 알고리즘 구현
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    merged.extend(left[l:])
    merged.extend(right[r:])
    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 입력 리스트 (1000000 크기)
arr = [random.randint(0, 10**6) for _ in range(1_000_000)]

# 실행 시간 저장할 리스트
times_bubble = []
times_merge = []
times_quick = []
times_timsort = []


# 1. 버블 정렬 실행 시간 측정
start_time = time.time()
bubble_sort(arr)
times_bubble.append(time.time() - start_time)
    
# 2. 퀵 정렬 실행 시간 측정
arr_copy = arr[:]
start_time = time.time()
quick_sort(arr)
times_quick.append(time.time() - start_time)

# 3. 병합 정렬 실행 시간 측정
arr_copy = arr[:]
start_time = time.time()
merge_sort(arr)
times_merge.append(time.time() - start_time)

# 4. Timsort 실행 시간 측정
arr_copy = arr[:]
start_time = time.time()
arr_copy.sort()  # 내장 Timsort 사용
times_timsort.append(time.time() - start_time)

# 결과 출력
print("버블 정렬 평균 시간:", times_bubble)
print("퀵 정렬 평균 시간:", times_quick)
print("병합 정렬 평균 시간:", times_merge)
print("Timsort 평균 시간:",times_timsort)

