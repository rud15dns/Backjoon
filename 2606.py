'''
그래프 : DFS에 대해서 공부해야할 필요
가야할 곳과 이미 간 곳을 구분해야 한다. 
1과 연결된 컴퓨터의 개수를 세는 것이다.
'''
n = int(input())
m = int(input())

arr = [0] * (n + 1)
arr[1] = 1

def dfs(graph, start):
    for key, value in graph.items():
        for elem in value:
            if arr[key] == 1 and arr[elem] != 1:
                arr[elem] = 1
                dfs(graph, elem)
            elif arr[elem] == 1 and arr[key] != 1:
                arr[key] = 1
                dfs(graph, key)
            
    return
    
    
    

graph = dict()
for i in range(m):
    a, b = map(int, input().split())
    if a in graph: #a에 해당하는 키가 있다면
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

# print(graph)
dfs(graph, 1)
# print(arr)
print(sum(arr)-1)