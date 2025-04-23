# 1000000개의 랜덤 숫자 리스트 생성
import random
arr = [random.randint(0, 10**6) for _ in range(1_000_000)]

# 1. timsort는 python 내장함수인 sort()를 사용한다. 
arr.sort()

#2. 병합 정렬로 sort
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

merge_sort(arr)

# 3. quick sort로 sort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] 
    return quicksort(left) + middle + quicksort(right)  

quicksort(arr)

# 4. bubble sort로 sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
bubble_sort(arr)