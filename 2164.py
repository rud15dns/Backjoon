#파이썬에서 리스트에서 in연산자가 O(n)이었던 것처럼, pop 또한 O(n)의 시간복잡도를 갖는다고 한다.
#deque 를 이용해보려고 한다. 덱. 앞뒤 출입이 자유롭게 가능하다.
#deque에서 popleft를 이용하면 pop(n)처럼 O(n)의 시간복잡도를 갖는 것이 아니라, 앞에서 바로 찾아서 출력하므로 O(1)의 시간복잡도를 갖는다.

from collections import deque
n = int(input())
dq = deque()

for i in range(1, n+1):
    dq.append(i)


while len(dq) != 1:
    dq.popleft()
    n = dq.popleft()
    dq.append(n)

print(dq[0])