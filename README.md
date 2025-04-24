# Team4_2025s_Algorithm 
알고리즘 중간고사 Team4
---

## 👥팀원

- 김수빈 (경영AI / 22200105)  
- 양찬 (ACE,DS / 22000415)  
- 유시현 (ICT&DS / 22000457)  
- 김찬우 (생명AI / 21900197)

---

## 🗂️ 브런치 및 파일 구조


| 브랜치 이름     | 설명                            | 포함 파일 예시                                  |
|----------------|----------------------------------|-------------------------------------------------|
| `main`         | 최종 문제 풀이 및 주요 파일 저장                     | `.gitignore`, `README.md`, `problem1.ipynb` 등        |
| `dev` | 전체적인 개발 관련 파일 저장          |  |
| `feature/problem1` | 문제 1번 관련 소스코드들 저장    | `Bubble_Sort.py`, `Insertion Sort.py` 등     |
| `feature/problem2` | 문제 2번 관련 소스코드들 저장 | `binary_search_iter.py` 등                     |
| `feature/problem3` | 문제 3번 관련 소스코드들 저장 | `frequency_sort.py` 등                     |
| `feature/problem4` | 문제 4번 관련 소스코드들 저장 | `dfs_code` 등                     |
| `feature/problem5` | 문제 5번 관련 소스코드들 저장 | `difference_visualize.py` 등                    |
| `feature/final` |추가 문제 관련 소스코드들 저장 |                      |

---

## 🛠️ 사용 언어

- Python 3.x

---

## 📋 시험 전 역할 분담

| 역할               | 담당자       | 설명 |
|--------------------|--------------|------|
| 팀장 (PM)          | 유시현       | Slack 및 PR 관리, 시간 체크, 전략 조율, 전 문제 리뷰 |
| 문제 1·2·3 담당     | 김수빈, 양찬 | 정렬, 이진 탐색, Counter 사용 문제 |
| 문제 4·5 담당       | 유시현, 김찬우 | DFS 재귀 및 대용량 처리 문제 |
| 최종 검토           | 전원         | 전체 코드 정리, 성능 테스트 및 검수 |
| 검수자              | 전원         | 제출 전 코드 실행 및 주석 점검 |

---

## ✅ 풀이한 문제 목록

| 문제 번호 | 문제 작성자 |
|-----------|--------------|
| problem1  | 양찬         |
| problem2  | 양찬         |
| problem3  | 김수빈       |
| problem4  | 유시현       |
| problem5  | 김찬우       |
| problem6  | 유시현       |

---

## 📌 파일 상세 설명 
### 1. 브런치 : main 
   
| 파일명 | 파일 설명|
|-----------|--------------|
| .gitignore |         |
| README.md | readme   |
| README.md |         |
| problem1.ipyb|1번 문제 최종 답안|
| problem2.ipyb|2번 문제 최종 답안|
| problem3.py|3번 문제 최종 답안|
| problem4.py|4번 문제 최종 답안|
| problem5.py|5번 문제 최종 답안|
| problem6.py|최종 문제 최종 답안|




### 2. 브런치 : feature/problem1
| 파일명 | 파일 설명|
|-----------|--------------|
| .gitignore |         |
| README.md | readme   |
| README.md |         |
| README.md |         |
| README.md |         |

### 3. 브런치 : feature/problem2
| 파일명 | 파일 설명|
|-----------|--------------|
| .gitignore |         |
| README.md | readme   |
| p3_source.py |  문제 3번 관련 소스 코드  |
| README.md |         |
| README.md |         |

### 4. 브런치 : feature/problem4
| 파일명 | 파일 설명|
|-----------|--------------|
| .gitignore |         |
| README.md | readme   |
| dfs_code.py |  dfs 알고리즘 관련 소스 코드 |
| obstacle_case.py |  문제 4번 장애물 추가 버전      |
| p4_sihyeon.py | 유시현 문제 4번 해결 (예제)  |
| problem4.py| 문제 4번 풀이 과정 파일 |
| rectangle_case.py |  grid가 직사각형일 경우 버전     |
| test.py | 깃허브 연동 테스트 파일  |

### 5. 브런치 : feature/problem5
| 파일명 | 파일 설명|
|-----------|--------------|
| .gitignore |         |
| README.md | readme   |
| README.md |         |
| README.md |         |
| README.md |         |

### 6. 브런치 : feature/final
| 파일명 | 파일 설명|
|-----------|--------------|
| .gitignore |         |
| README.md | readme   |
| README.md |         |
| README.md |         |
| README.md |         |

### 7. 브런치 : dev
| 파일명 | 파일 설명|
|-----------|--------------|
| .gitignore | gitignore        |
| README.md |  readme      |
| test.py |   github 연결 확인용     |

## 문제 해결 과정 설명
##  1번 문제 (작성자 : )
---
##  2번 문제 (작성자 : )
---
##  3번 문제 (작성자 : )
---
##  4번 문제 (작성자 : 유시현 )
dfs 알고리즘을 사용하여 0에 도달하면 루프가 멈추게 되고, 찾지 못하면 false를 반환하며 찾지 못하였다는 신호와 멈추게 된다. 
방문 리스트를 만들어 각 좌표에 방문했는지 안했는지를 체크하고, 방문 한 경우 path 기록을 path 리스트에 저장한다.
모든 방문이 끝나고 0을 찾으면 True를 반환하며 재귀 루프를 탈출하게 되고, 방문한 기록들을 출력하여 어떤 과정을 거쳐 0에 도달하였는지 찾아내었다.
또한 step 은 각 좌표의 숫자를 의미하고, 그 숫자만큼 방향으로 나아가도록 설정하였다.

하지만, 문제에서 요구한 0을 찾는 모든 경우의수를 고려한 후 가장 최적의 답을 찾는 것은 해결하지 못하였다.
위치를 옮길 떄마다 모든 방향을 고려해야하는데, 현재 코드에서는 한 방향으로만 찾고 끝내어 해당 문제를 해결하지 못한다.
for 루프를 사용하여 모든 방향을 고려하도록 코드를 구성해보려고하였지만 성공하지 못하였다. 
현재 출력되는 경로의 숫자 합은 119라서 답안 제출을 119로 적어서 제출하였다.

---
##  5번 문제 (작성자 : )
---
##  추가 문제 (작성자 : )
---