'''
처음 든 생각은 set으로 풀어볼까? 이후 든 생각은 같은 거 나오면은 SET은 중복 허용이 안되어서 안되겠다!
인터넷에 찾아보니 파이썬을 위한 heapq가 있더라.
한번 이참에 이용해보도록 하겠다. 
'''
import sys
import heapq

n = int(input())
arr = []

for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            elem = heapq.heappop(arr)
            print(elem) 
    else:
        heapq.heappush(arr, x)
    

    