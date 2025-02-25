import sys
from collections import deque

## 데크로 바꿔서 시간 초과 해결 -> deque는 pop 시에 O(1)

input = sys.stdin.readline

m, n = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

## 배열 저장
arr = deque()
for _ in range(n):
    arr.append(list(map(int, input().split())))

## 토마토가 들어있는 위치 탐색
idx = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            idx.append((i, j, -1))


## bfs
def bfs(arr):
    if len(idx) == 0:
        return -1
    
    while idx:
        x, y, step = idx.popleft()
        step += 1

        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if (cx < 0 or cx >= n)  or (cy < 0 or cy >= m):
                continue

            if arr[cx][cy] == -1 or arr[cx][cy] == 1:
                continue

            else:
                arr[cx][cy] = 1
                idx.append((cx, cy, step))

    ## 개선
    for row in arr:
        if 0 in row:
            return -1
    
    return step

print(bfs(arr))
# result = bfs(arr)
# if result == -1:
#     print(result)
# else:
#     for i in range(n):
#         for j in range(m):
#             if arr[i][j] == 0:
#                 result = -1
    
#     print(result)