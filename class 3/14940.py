# 처음에는 디피로 접근했었는데, update를 어떻게 해야할지 감이 안왔음.
# bfs를 이용하고, score 변수를 이용해서 점수를 저장함. 이름만 다를 뿐 visited의 역할을 함. 

import sys
from collections import deque
input = sys.stdin.readline

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
n, m = map(int, input().split())

map = [list(map(int, input().split())) for _ in range(n)]
routes = [ [-1] * m for _ in range(n)]

bools = True
# 시작점 위치(2) 찾기
for i in range(n):
    for j in range(m):
        if map[i][j] == 2 and bools:
            dst_x, dst_y = i, j
            bools = False
            break

    if not bools:
        break


def bfs(start_x, start_y):
    dq = deque()
    dq.append((start_x, start_y))
    routes[start_x][start_y] = 0

    while dq:
        cx, cy = dq.popleft()

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and routes[nx][ny] == -1 and map[nx][ny] == 1:
                routes[nx][ny] = routes[cx][cy] + 1
                dq.append((nx, ny))

    

bfs(dst_x, dst_y)
for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            print(0, end = ' ')
        elif map[i][j] != 0 and routes[i][j] == -1:
            print(-1, end = ' ')
        else:
            print(routes[i][j], end = ' ')
    print()