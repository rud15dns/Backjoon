#벽과 상하좌우? 약간 미로탐색의 느낌이 난다.
# 현재 위치에서 x, y 해서 dx, dy +=1 -=1 이렇게 이용하면 편할지도
#directions를 dx, dy 로 해서 for문으로 푸는 게 생각이 안 났었다.
#그리고 visited를 표현해야한다는 기본적인 사실도 까먹었었다. 반성하자.
#an

#시간초과났다.
#중복되어 탐색하고 있었다. 나는 조건때문에 중복이 상관없다고 생각했었는데,
# 기준점만 중복을 탐색하고, 나머지 양옆에 있는 점들을 중복을 체크해주지 않아서,
# 계속해서 중복 탐색을 했던 것이다.  

n, m = map(int, input().split())

mapped = [input() for _ in range(n)]
ax, ay = 0, 0 #출발점 위치초기화
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
points = []

#출발점의 위치를 찾는다.
for i in range(n):
    for j in range(m):
        if mapped[i][j] == "I":
            ax, ay = i, j

points.append((ax, ay))
visited = set()

cnt = 0

#상하좌우로 이동
while points:
    x, y = points.pop()

    visited.add((x, y))
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if (nx, ny) not in visited and 0 <= nx < n and 0 <= ny < m and mapped[nx][ny] != "X":

            if mapped[nx][ny] == "P":
                cnt += 1

            visited.add((nx, ny))
            points.append((nx, ny))
      

if cnt == 0:
    print("TT")
else:
    print(cnt)

        
        

