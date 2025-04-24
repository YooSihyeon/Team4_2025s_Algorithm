# 등장 빈도 + 우선순위 정렬
def count_with_dict(numbers):
    freq_dict = {}  #딕셔너리 생성
    for num in numbers:
        # 기존에 없으면 0으로 초기화 후 +1
        freq_dict[num] = freq_dict.get(num, 0) + 1
    return freq_dict

# (숫자, 빈도수) 정렬하는 함수
def sort_by_frequency(freq_dict):
    # 1순위: 등장 횟수 내림차순 (-x[1])
    # 2순위: 숫자 오름차순 (x[0])
    return sorted(freq_dict.items(), key=lambda x: (-x[1], x[1]))


if __name__ == "__main__":
    n = int(input())  # 리스트에 적한 숫자의 개수?
    numbers = list(map(int, input().split()))  # 숫자 리스트 입력 받기

    # 빈도수 계산 → 정렬 → 출력
    freq_dict = count_with_dict(numbers)
    sorted_items = sort_by_frequency(freq_dict)

for item in sorted_items:
    print(item)  # (숫자, 빈도수) 튜플 형태