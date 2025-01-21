import sys
input = sys.stdin.readline

t = int(input()) 
map = [ list(input().rstrip()) for _ in range(t) ]
directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

visited = set()
scores = {} #단지마다 점수 관리
idx = 0

def bfs(x, y):
    global idx
    queue = [(x, y)] # list((x, y)) 로 해버리면 => [x, y] 로 저장된다. 
    visited.add((x, y))
    scores[idx] = 1

    while queue:
        (cx, cy) = queue.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if (0 <= nx < t and 0 <= ny < t) and (nx, ny) not in visited:
                visited.add((nx, ny))

                if map[nx][ny] == "1":
                    queue.append((nx, ny))
                    scores[idx] += 1


for i in range(t):
    for j in range(t):
        if (i, j) not in visited and map[i][j] == "1":
            bfs(i, j)
            idx += 1

print(len(scores.values()))
scores_list = sorted(list(scores.values()), reverse=False)

for elem in scores_list:
    print(elem)