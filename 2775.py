#a층의 b호에 살려면, a0b호 이려면, (a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와야 한다.
#0층의 i호에는 i명이 산다.
#아래서부터 천천히 덧셈을 해가서, 총 k층의 n호까지 계산을 해야한다. 
#1차시도 : 시그마 덧셈 계산 -> 소수점이 나와서 다른 방법 계산
#2차시도 : 2차원의 배열에서 왼쪽, 아래쪽의 합과 같음. 15 * 15라면 그냥 배열을 계산하는 게 빠를듯하다.

'''
 0 1 2 3 4 
0
1
2
3
4

일 때, arr[1][1] = arr[1][0] + arr[0][1]인 것처럼 이를 식으로 바꾸면,
arr[i][j] = arr[i-1][j] + arr[i][j-1]이다.

'''

arr = [[0] * 15 for i in range(15)]
#arr 계산
for i in range(15):
    for j in range(1, 15):
        if i == 0:
            arr[i][j] = j
        else:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    print(arr[k][n])
