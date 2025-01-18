import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

#모든 엣지를 INF로 설정. (길을 모르는 상태이므로)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 향하는 것은 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0


#엣지에 대한 비용 추가
for _ in range(m):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

#중간에 거쳐갈 노드들 => k => 직접적으로 연결되어 있지 않으면, INF이므로, 알아서 거쳐가는 걸로 저장될 것임.
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

#케빈 베이컨의 수와 그 사람의 번호 사용
shortest = []
for i in range(1, n + 1):
    a = i
    #sum도 함수 사용이 가능
    b = sum(x for x in graph[i] if x != INF)
    shortest.append([a, b])

print(min(shortest, key=lambda x: (x[1], x[0]))[0])