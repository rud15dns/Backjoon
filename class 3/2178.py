# # 좌수법과 스택을 이용하면 되겠다.
# # 최소로 이동하려면, 아래, 우측 방향을 우선으로 이동해야한다. 
# # string은 불변타입이라서, list()를 붙여주지 않고는 수정이 불가능하다.
# # map이 공유될 수 있다.

# points = [(0,0)] #최종적으로 지나가는 점의 위치
# points_1 = [(0,0)]

# import sys
# input = sys.stdin.readline 

# from copy import deepcopy

# n, m = map(int, input().split())
# map = [list(input().rstrip()) for _ in range(n)]
# map2 = deepcopy(map)

# cx, cy = 0, 0
# dest_x, dest_y = n - 1, m - 1

# def down(cx, cy, map, point):
#     while cx != dest_x or cy != dest_y: #목표점에 도달할 때까지
#         point.append((cx, cy))
#         # print(point)
#         if cx + 1 < n and (cx + 1, cy) not in point and map[cx + 1][cy] == "1": #아래 방향
#             cx = cx + 1

#         elif cy + 1 < m and (cx, cy + 1) not in point and map[cx][cy + 1] == "1": #오른쪽 방향
#             cy = cy + 1

#         elif cy - 1 >= 0 and (cx, cy - 1) not in point and map[cx][cy-1] == "1":
#             cy = cy - 1

#         elif cx - 1 >= 0 and (cx - 1, cy) not in point and map[cx-1][cy] == "1": #범위 내고, 가본 적이 없다면
#             cx = cx - 1

#         else:
#             map[cx][cy] = "0" #다시는 못가도록
#             if (cx, cy) == (1, 0)  or (cx, cy) == (0, 1):
#                 (cx, cy) = point.pop()
#             else:
#                 point.pop()
#                 (cx, cy) = point.pop()


#     point.append((cx, cy))

# def right(cx, cy, map, point):
#     while cx != dest_x or cy != dest_y:
#         print(point)
#         if cy + 1 < m and (cx, cy + 1) not in point and map[cx][cy + 1] == "1": #오른쪽 방향
#             cy = cy + 1
#             point.append((cx, cy))

#         elif cx + 1 < n and (cx + 1, cy) not in point and map[cx + 1][cy] == "1": #아래 방향
#             cx = cx + 1
#             point.append((cx, cy))

#         elif cy - 1 >= 0 and (cx, cy - 1) not in point and map[cx][cy-1] == "1":
#             cy = cy - 1
#             point.append((cx, cy))

#         elif cx - 1 >= 0 and (cx - 1, cy) not in point and map[cx-1][cy] == "1":
#             cx = cx - 1
#             point.append((cx, cy))

#         else:
#             map[cx][cy] = "0"
#             (cx, cy) = point.pop()

#     point.append((cx, cy))

# # down(0, 0, map, points)
# right(0, 0, map2, points_1)
# print(len(points_1))

# # print(min(len(points), len(points_1)))

# # 이코드의 문제점 -> 결국에는 우선순위를 정해버리니까, 최단 거리를 찾지 못한다는점...
# # 지피티에게 물어보니까, bfs로 풀라고 한다. (bfs 는 네방향 모두를 동일하게 생각하기 때문이다.)
#덱이라는 특성과(가장 작은 distance인 것이 가장 앞에 있는), BFS라는 특성(모든 방향에 대해서 동일한 우선순위를 가지는) 덕분에 해결이 가능하다.

from collections import deque

def bfs(cx, cy, dest_x, dest_y, n, m, map):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set() # 이전에 한번이라도 방문한 적이 있는지
    queue = deque([(cx, cy, 0)]) # 현재위치, 거리

    while queue:
        x, y, dist = queue.popleft()
        if x == dest_x and y == dest_y:
            return dist+1
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and map[nx][ny] == "1":
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))


n, m = map(int, input().split())
map = [list(input().rstrip()) for _ in range(n)]

start_x, start_y = 0, 0
dest_x, dest_y = n - 1, m - 1
result = bfs(start_x, start_y, dest_x, dest_y, n, m, map)
print(result)