'''
알고리즘 생각
1. sub(2) -> sub(1) -> sub(0) -> 1
    sub(2) -> sub(0) -> 1
    sub(1) -> sub(0) -> 1
    sub(0) -> 1

2. n-1, n-2, n-3일 때를 각각 세면 되겠다는 생각이들었다.
3. 재귀를 이용하고 base조건을 사용해서 딱 0이 될 때까지만 case로 세었다. 
4. 아직 더 뺄 수 있는 조건일 때는, 계속해서 계산을 지속하였다.
'''

def sub(n):
    sum = n
    if sum < 0:
        return 0
    
    if sum == 0:
        return 1
    else:
        return sub(n-1) + sub(n-2) + sub(n-3)

import sys

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(sub(n))