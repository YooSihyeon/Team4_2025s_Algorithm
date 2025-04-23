import random
import time
import matplotlib.pyplot as plt

original_data = random.sample(range(0, 10**7), 1000000)  # 1000000만개 숫자 리스트 

def merge_sort(arr): # 병합정렬 코드 
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right): # 병합 함수 
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result.extend(left[l:])
    result.extend(right[r:])
    return result

def quick_sort(arr): # 퀵 정렬 코드
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def counting_sort(arr, exp): # 기수정렬 코드 일부 
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in arr:
        index = (i // exp) % 10
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in reversed(range(n)):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr): # 기수정렬 코드
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr
