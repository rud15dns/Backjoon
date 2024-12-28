'''
DFS 공부한 것을 이용해서 한번 풀어보자
문제점 : 시작점이 어느 점과도 연결되지 않은 경우 출력 X
'''
import sys

vertex, edge, start_node = map(int, input().split())
graph = dict()

for _ in range(edge):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if a not in graph.keys():
        graph[a] = [b]
    else:
        graph[a].append(b)
    if b not in graph.keys():
        graph[b] = [a]
    else:
        graph[b].append(a)

# for key in graph:
#     graph[key].sort(reverse=False)

#deque version
print(graph)
def dfs(graph, start_node):
    from collections import deque
    visited = []
    have_to_visited = deque([start_node])

    while have_to_visited:
        node = have_to_visited.popleft()
        if node not in visited:
            visited.append(node)
            if node in graph.keys():           
                have_to_visited.extendleft(reversed(graph[node]))

    return visited

#recursive version
def dfs_r(graph, start, visited = []):
    visited.append(start)
    print(visited)
    if start in graph.keys():
        for node in graph[start]:
            if node not in visited:
                dfs_r(graph, node, visited)
    
    return visited

dfs_order = list(dfs(graph, start_node))
dfs_order = list(dfs_r(graph, start_node, visited=[]))

for elem in dfs_order:
    print(elem, end = ' ')