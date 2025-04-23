import random
import time
import matplotlib.pyplot as plt
import numpy as np

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
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

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def counting_sort(arr, exp):
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

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

# 입력 크기 설정
n_values = np.arange(100, 10001, 100)

# 각 정렬별 실행 시간 저장
times_quick = []
times_merge = []
times_radix = []
times_sort = []
times_sorted = []

for n in n_values:
    arr = [random.randint(0, 100000) for _ in range(n)]

    # Quick Sort
    start = time.time()
    quick_sort(arr[:])
    times_quick.append(time.time() - start)

    # Merge Sort
    start = time.time()
    merge_sort(arr[:])
    times_merge.append(time.time() - start)

    # Radix Sort
    start = time.time()
    radix_sort(arr[:])
    times_radix.append(time.time() - start)

    # list.sort() (in-place)
    start = time.time()
    arr_copy = arr[:]
    arr_copy.sort()
    times_sort.append(time.time() - start)

    # sorted() (새 리스트)
    start = time.time()
    sorted(arr[:])
    times_sorted.append(time.time() - start)

# 그래프 시각화
plt.figure(figsize=(12, 6))
plt.plot(n_values, times_quick, label="Quick Sort", marker="o")
plt.plot(n_values, times_merge, label="Merge Sort", marker="s")
plt.plot(n_values, times_radix, label="Radix Sort", marker="^")
plt.plot(n_values, times_sort, label="list.sort()", marker="D")
plt.plot(n_values, times_sorted, label="sorted()", marker="x")

plt.yscale("log")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Sorting Algorithm Performance Comparison")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()