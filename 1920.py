# 시간 초과의 이유가...
# 파이썬에서는 in 연산자를 리스트에 사용하면 O(N)으로 원본 코드는 O(NM)의 시간복잡도를 가진다.
#set이나 dict에서는 in 연산자의 시간복잡도가 O(1)이다. 
#set에서는 index가 없어서 고민이 컸지만, 그런 경우에는 애초에 in의 대상이 되는 arr만을 set으로 바꿔주면 되지 않나? 라는 생각.

import sys

n = sys.stdin.readline().rstrip()
arr = set(map(int, input().split()))

m = int(sys.stdin.readline().rstrip())
arr_2 = list(map(int, input().split()))

for i in range(m):
    if arr_2[i] in arr:
        print(1)
    else:
        print(0)