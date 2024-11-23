'''
selected랑 not_selected랑 나누면은 충분하지 않을까? 라고 생각했는데
그리고, set으로 선택해서 중복된 거는 없애면 되지 않을까? 라고 생각했지만,

아무리 생각해도 이렇게 풀면은 안되고 그래프를 만들어야만 하겠다는 생각이 들었다.
서로의 연결된 것을 넣지 않으면은, 하나가 어디까지 연결되어있는지 알기가 어렵다.

DFS를 쓰는 게 그런 의미에서 좋을 것 같다.

n, m = map(int, input().split())
not_selected = [tuple(map(int, input().split())) for _ in range(m)]

not_selected.sort(key=lambda x: x[0])  # 간선 순서 정렬

selected = set()  # 선택된 노드들
cnt = 0

for u, v in not_selected:
    if u in selected or v in selected:
        selected.add(u)
        selected.add(v)
    else:
        # 새로운 연결 요소를 발견
        selected.add(u)
        selected.add(v)
        cnt += 1

# 간선에 포함되지 않은 나머지 노드들에 대해 새로 연결 요소를 추가
for i in range(1, n + 1):
    if i not in selected:
        cnt += 1
        selected.add(i)

print(cnt)'''
#Keyerorr 발생 : 딕셔너리에 해당하는 Key가 없을 때 접근하는 경우
#for 문에서 range(i)로 순서대로 접근했는데, 생각해보니 21 61 처럼 꼭 v가 2개라도 순서대로가 아니다. 
#틀리면 문제조건부터 다시읽고, 어떻게 고치면 좋을지 계속 생각해봐야겠다.
#dfs 는 need_visited배열을 만들지 말고, 바로 for elem in graph로 넘어가도 되는데, 이때, graph에 있는지 없는지를 살펴보아야한다. 

import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
graph = dict()

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a not in graph:
        graph[a] = set()
    
    if b not in graph:
        graph[b] = set()
    
    graph[a].add(b)
    graph[b].add(a)

visited = list()
# print(graph)

def dfs(node):
    # print(visited)
    if node not in visited:
        visited.append(node)
    
    if node in graph:
        for a in graph[node]:
            if a not in visited:
                dfs(a)

cnt = 0

for i in range(1, n + 1):
    if i not in visited:
        dfs(i)
        cnt += 1

print(cnt)