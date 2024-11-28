#이거 내 생각에는 k를 계속해서 반복문 돌리는? 반복문 안에 반복문 이런 식으로 풀어야 할 것 같다.
import sys
n = int(input())

for _ in range(n):
    m = int(input())
    
    graph = dict()  
    for _ in range(m):
        value, key = sys.stdin.readline().rstrip().split()
        if key not in graph:
            graph[key] = [value]
        else:
            graph[key].append(value)

    # print(graph)
    tot = 0
    mul = 1

    
    for i in graph.keys():
        
        mul *= len(graph[i])
        tot += len(graph[i])

            
    if len(graph) > 1:   
        print(mul + tot)
    else:
        print(tot)
    
    