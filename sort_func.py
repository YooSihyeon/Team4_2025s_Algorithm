import random
numbers = [random.randint(0, 9999) for _ in range(100)]

# 병합 정렬 (Merge Sort)
def merge_sort(arr):
    # 종료 조건: 리스트의 길이가 1 이하이면 이미 정렬된 상태이므로 반환
    if len(arr) <= 1:
        return arr

    # 리스트를 절반으로 나누기
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # 왼쪽 절반을 재귀적으로 정렬
    right = merge_sort(arr[mid:])  # 오른쪽 절반을 재귀적으로 정렬

    # 정렬된 두 부분 리스트를 병합하여 반환
    return merge(left, right)

# 병합 함수: 두 정렬된 리스트를 하나의 정렬된 리스트로 합침
def merge(left, right):
    result = []  # 병합 결과를 저장할 리스트
    i = j = 0    # left, right 리스트의 인덱스 초기화

    # 두 리스트의 요소를 하나씩 비교하며 정렬된 순서로 추가
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])  # 더 작은 값을 결과 리스트에 추가
            i += 1
        else:
            result.append(right[j])  # 더 작은 값을 결과 리스트에 추가
            j += 1

    # 남은 요소들(어느 한 쪽 리스트가 먼저 끝났을 경우)을 결과 리스트에 추가
    result.extend(left[i:])   # left 리스트의 남은 부분
    result.extend(right[j:])  # right 리스트의 남은 부분
    return result  # 병합된 결과 반환

# 퀵 정렬 코드 
def quick_sort(arr):
    # 종료 조건: 리스트의 길이가 1 이하이면 이미 정렬된 상태이므로 그대로 반환
    if len(arr) <= 1:
        return arr

    # Pivot(기준 값)을 리스트의 중간값으로 설정
    pivot = arr[len(arr) // 2]

    # 리스트를 Pivot을 기준으로 나누기
    left = [x for x in arr if x < pivot]     # Pivot보다 작은 값들
    middle = [x for x in arr if x == pivot]  # Pivot과 같은 값들
    right = [x for x in arr if x > pivot]    # Pivot보다 큰 값들

    # 재귀 호출을 통해 left와 right를 정렬하고, middle과 함께 합쳐서 반환
    return quick_sort(left) + middle + quick_sort(right)

# 기수정렬 radix sort
def counting_sort(arr, exp):
    # 리스트 길이 n을 구함
    n = len(arr)

    # 정렬된 결과를 저장할 리스트 (출력용)
    output = [0] * n

    # 0~9까지의 숫자 개수를 저장할 배열 (0~9까지 10개 자리)
    count = [0] * 10

    # 1. 현재 자릿수를 기준으로 숫자 개수를 count 배열에 저장
    for i in arr:
        index = (i // exp) % 10  # 현재 자릿수 추출 (예: 170에서 10의 자리 → (170 // 10) % 10 = 7)
        count[index] += 1  # 해당 자릿수 등장 횟수 증가

    # 2️. count 배열을 업데이트하여, 해당 숫자가 정렬될 위치를 계산
    for i in range(1, 10):
        count[i] += count[i - 1]  # 현재 숫자의 누적 개수를 저장

    # 3️. 배열을 역순으로 순회하며 output 배열에 정렬된 결과 저장
    i = n - 1  # 마지막 요소부터 시작 (안정 정렬을 위해 오른쪽에서 왼쪽으로 이동)
    while i >= 0:
        index = (arr[i] // exp) % 10  # 현재 자릿수 추출
        output[count[index] - 1] = arr[i]  # 현재 숫자를 output 배열의 해당 위치에 저장
        count[index] -= 1  # count 배열 업데이트 (중복된 숫자 처리를 위해 감소)
        i -= 1  # 다음 숫자로 이동

    # 4️. 정렬된 output 배열을 원래 배열(arr)에 복사 (in-place 정렬)
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # 배열에서 최댓값을 찾아, 몇 자리 숫자인지 확인
    max_num = max(arr)

    # exp(자리수 단위)를 1부터 시작하여, 최댓값의 자릿수를 넘어갈 때까지 반복
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)  # 현재 자리수를 기준으로 계수 정렬 수행
        exp *= 10  # 다음 자릿수로 이동 (1 → 10 → 100 ...)

    return arr  # 최종 정렬된 리스트 반환

#print("병합 정렬로 정렬된 리스트:", merge_sort(numbers))
#print("퀵 정렬로 정렬된 리스트:", quick_sort(numbers))
#print("기수 정렬로 정렬된 리스트:", radix_sort(numbers))