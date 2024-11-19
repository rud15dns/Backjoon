'''
내가 알고리즘을 생각한 게 있었는데, 그 방법이 맞긴한데, 어떻게 구현해야할지 모르겠어서
인터넷을 결국 참고하고 말았다.

결국 그 방법은 맞았다.
n/2만큼 네 개의 점이 계속해서 빙글뱅글 돌면서, 본인의 색과 일치한지를 파악하는 게 우선이었다.
근데 아무래도 좀 모르겟어가지고,,, 결국에는 남의 코드를 참고하고 말았다.
divide and conquer는 재귀적으로 자신을 호출하면서 연산의 단위를 조금씩 줄여가는 연산이라고 한다.
여기서 가장 중요한 아이디어는 결국에는, i부터 N까지 도는데, 그 때가 맨 처음에 시작점이 된 x,y하고, i,j의 색깔이 같은지를 파악하면
되는 부분이었다. i, j의 색깔이 끝까지 같은데 white면은 화이트 변수 또는 화이트 배열에다가 +해주고,
blue면은 blue 변수 또는 블루 배열에다가 +해주면 된다.
조금 외우긴 했지만, 일단 코드를 짜보자.
'''
import sys 

n = int(input())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

count_white = 0
count_blue = 0


def div_and_conq(x, y, range_N):
    global count_white, count_blue

    color = arr[x][y]
    for i in range(x, x + range_N):
        for j in range(y, y + range_N):
            if color != arr[i][j]: #내 옆하고 다르면은 반을 자를 수밖에 없는 
                div_and_conq(x, y, range_N//2)
                div_and_conq(x + range_N//2, y, range_N//2)
                div_and_conq(x, y + range_N//2, range_N//2)
                div_and_conq(x+range_N//2, y+range_N//2, range_N//2) 
                return #색상이 다르면은 밑에 연산에 포함되면 안되므로 return이 필수적                     

    
    if color == 0:
        count_white += 1
    else:
        count_blue += 1

div_and_conq(0,0,n)
print(count_white)
print(count_blue)


