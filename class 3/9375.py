#이거 내 생각에는 k를 계속해서 반복문 돌리는? 반복문 안에 반복문 이런 식으로 풀어야 할 것 같다.
#이라고 생각했지만, 사실 안 입는 경우도 포함시킨다음에, 0 0 0 0 0인 그런 경우만 하나 빼면 되기 때문에
#풀 수 있었다.

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

    mul = 1

    
    for i in graph.keys():
        
        mul *= (len(graph[i]) + 1)

            
    print(mul - 1)
    
    