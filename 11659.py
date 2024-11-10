#set을 쓰기에는, set자체가 중복을 허락하지 않기 때문에 리스트가 나아보임.
# total = sum(arr[i-1:j]) #문자열을 자르는 것은 기본적으로 O(M), N번 반복하니 O(NM)
# 누적합 알고리즘에 대해서 알아보자.
'''
A~B까지의 값을 구하기 위해서
먼저 누적합 배열을 만들어준 다음
B까지의 누적합 - A-1까지의 누적합을 실시한다.

O(N) - arr_cum을 만드는 데 필요한 시간
O(M) - arr_cum에 접근하는 게 각각 O(1) 이고, 그것이 M번 반복
=> 총 O(N + M)의 시간복잡도를 만든다. 
'''
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int,sys.stdin.readline().rstrip().split()))

arr_cum = [0] * (n)
arr_cum[0] = arr[0]
for i in range(1, n):
    arr_cum[i] += arr_cum[i-1] + arr[i]


for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    if i - 2 < 0:
        print(arr_cum[j-1])
    else:
        print(arr_cum[j - 1] - arr_cum[i - 2])