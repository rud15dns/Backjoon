'''
여러모로 어려웠던 문제이다. 
일단은 dp를 제대로 쓰지 못하는 것 같아서, 다른 사람의 아이디어를 가져왔고,
그대로 가져왔는데, 계속해서 틀렸다고 하여서 고치는데 시간이 걸렸다.
챗지피티도 오류를 못잡아냈었는데, 생각해보니까, 6의 배수일 때는 무조건 2로만 나뉘게 되어있어서,
더 나은 방법이 있음에도 그렇게 시도하지 못할 뻔 했던 것이다.
dp[i] = (dp[i-1] (이전 것), dp[i//2] (2로 나누었던 것까지의 덧셈), dp[i//3] (3으로 나누었던 것까지의 덧셈))

일단 dp의 배열을 2부터 시작해서 n+1까지 만드는 게 핵심인 것 같다.
down-up인 셈이다. 
'''

dp = [0] * (10 ** 6 + 2)
n = int(input())

dp[0] = 0
dp[1] = 0

for i in range(2, n + 1):
    if (i % 2 == 0 and i % 3 == 0):
        dp[i] = min(dp[i-1], dp[i//2], dp[i//3]) + 1
    elif (i % 2 == 0):
        dp[i] = min(dp[i-1], dp[i//2]) + 1
    elif (i % 3 == 0):
        dp[i] = min(dp[i-1], dp[i//3]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[n])