'''
dictionary를 1학년 이후로 거의 처음써서 인터넷에서 레퍼런스를 참고하였다.
dict = {} 로 생성하고,
만약에 elem in dict, 여기서 elem은 key를 의미하는 것이고, 해당하는 키가 있다면,
dict[elem] 즉 value값을 += 1하고,
없다면 dict[elem] = 1로 직접 dict에 추가하는 것으로 문제를 풀었다.

위와 같은 딕셔너리의 개념을 상기시키고 나니까, 
밑에 있는 것은 응용해서 풀 수 있었다. 
'''

import sys
n = int(input())
arr= list(map(int, sys.stdin.readline().rstrip().split()))

dict = {}

for elem in arr:
    if elem in dict:
        dict[elem] += 1
    else:
        dict[elem] = 1
    
m = int(input())
arr_2 = list(map(int, sys.stdin.readline().rstrip().split()))
for elem in arr_2:
    if elem in dict:
        print(dict[elem], end = ' ')
    else:
        print(0, end = ' ')