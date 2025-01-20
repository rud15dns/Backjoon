# heapq 를 이용하자. 
# (절대값, 원래 값)을 기준으로 heap에 넣으면, 절대값이 작은 순으로 정렬된다.
# 파이썬에서 heapq가 최소힙을 만든다는 것을 유의해야겠다. 
# 시간 초과는 input 때문.

import heapq
import sys

input = sys.stdin.readline
heap = []

x = int(input())
for _ in range(x):
    a = int(input())

    if a != 0:
        heapq.heappush(heap, (abs(a), a))

    elif a == 0 and len(heap) != 0:
        x, y = heapq.heappop(heap)
        print(y)
    
    else:
        print(0)