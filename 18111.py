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

n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

min_high = 257
max_high = -1

min_time = 10000000000000
result = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] > max_high:
            max_high = arr[i][j]
        if arr[i][j] < min_high:
            min_high = arr[i][j]

for h in range(min_high, max_high + 1):
    temp_time = 0
    b_prime = b
    condition = False

    for i in range(n):
        for j in range(m):
            if arr[i][j] - h > 0:
                temp_time += 2 * (arr[i][j] - h)
                b_prime += (arr[i][j] - h)
                condition = True

            elif b_prime > 0 and arr[i][j] - h < 0:
                temp_time += (abs(arr[i][j] - h))
                b_prime -= abs(arr[i][j] - h)
                condition = True


    if b_prime < 0 or condition == False:
        continue
            
    if min_time > temp_time:
        min_time = temp_time
    
    if min_time == temp_time:
        result = max(result, h)

print(min_time, result)