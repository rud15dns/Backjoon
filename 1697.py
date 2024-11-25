'''
처음에는 당연히 dp문제라고 생각했었다.
근데 약간 골치아파진게 뒤로 이동하고 앞으로 이동하는 건데, 괜찮을까? 였다.
약간 1초 뒤에 제일 먼곳, 뭐 이런 식으로 찾으려고 해서 맞겠지? 하고 알고리즘 분류 보니까
그래프란다.

아하!
처음부터 분기가 계속 나뉘어져서 그래프인가보구나. 
이렇게 생각해야하는구나 싶었다.
그렇다면 BFS를 사용하는 게 맞겠다! 싶었다.
왜냐하면 같은 초(같은 분기 수)에 따라서 나누어질테니까 말이다.
더 이상 들어갈 수 없을 때 그 때의 초를 정답으로 하면 되지않을까?

뭔가 한번에 여러개를 처리하고 싶었고, 계속 3개만 생각하니까, 3? i * 3 이런 식으로 j를 해야하나? 싶었는데,
챗지피티의 코드를 잠깐 슬적 도움을 받아서 보자면,
기본 흐름 그대로에다가 3개가 아니라, dq에 들어있는 노드의 개수 하면 같은 레벨의 것들이니까 충분히 쉽게 풀 수 있었던 것이다.
자 메모리 초과가 났다. 

그렇다면 이미 지나간 곳에 대해서 또 지나갈 필요가 잇을까?
지나간 노드에 대해서는 똑같은 분기가 세 개 펼쳐질텐데?
지나갔던 곳은 안 지나가도 되겠다.

꼭 BFS 를 코드로 외우지 않고, 그림으로 외워야
이런 흐름이 금방 나오겠다 싶다.

언제나 항상 3개가 분기될 이유도 없으므로, 노드의 개수만큼 한 레벨에 있다고 생각하는게,
BFS의 핵심인 것 같다. 

'''
from collections import deque
n, m = map(int, input().split())

dq = deque()
dq.append(n)
visited = [0] * (100000 + 1)

time = 0 
while dq:
    size = len(dq)
    for _ in range(size):
        node = dq.popleft()
        visited[node] = 1

        if node == m:
            print(time)
            exit()
        
        if node + 1 <= 100000 and visited[node + 1] == 0:
            dq.append(node+1)
        
        if node - 1 >= 0 and visited[node - 1] == 0:
            dq.append(node-1)
        
        if 2*node >= 0 and 2*node <= 100000 and visited[node * 2] == 0:
            dq.append(2*node)

    time += 1
    
print(time)