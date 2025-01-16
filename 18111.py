# 1. 결국에는 N x M 의 모든 값이 같아야한다.
# 2. 같게 만드는데, -1일 때는 2초, 그리고 B += 1
# 3. +1일 때는 1초, 그리고 B -= 1

# 최소 시간을 구하라. (같은 시간이라면, 땅의 높이가 높은 경우를 구하라)
# - 가능한 최소 높이부터 최대 높이까지를 계산하면서 최적의 높이를 찾아야한다.
# 최솟값 범위와 최댓값 범위 찾아서

#문제점 : 가장 높은 곳에서부터 회수하는 로직을 추가해보는 걸로
#문제되는 테스트 케이스
# 3 3 0
# 23 21 17
# 44 18 29
# 25 16 32

#중요한 것은 2차원을 1차원으로 바꿔버려서, min, max를 간편하게 사용할 수 있었던 것
#모든 높이를 탐색할 필요없이, 최소부터 최대까지 해서 그 중에서 맞추면 된다는 점 -> 결국에는 브루트포스라는 점
#블럭의 개수를 이용해서 점화식으로 표현하면, 좀 더 편하게 구할 수 있다는 점
import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr_flat = [arr[i][j] for i in range(n) for j in range(m)]
result = []

min_high = min(arr_flat)
max_high = max(arr_flat)

min_time = 10000000000000


for h in range(min_high, max_high + 1):
    remove = 0
    add = 0

    b_prime = b

    for elem in arr_flat:
        if elem - h > 0:  #블럭 제거 시
            remove += (elem - h)
        
        elif elem - h < 0: #블럭 추가 시
            add += abs((elem - h))

    if b_prime - (add) + remove >= 0:
        temp_time = remove * 2 + add

        result.append([temp_time, h])

result2 = min(result, key=lambda x: (x[0], -x[1]))
print(result2[0], result2[1])