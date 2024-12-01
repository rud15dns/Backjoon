# 전에 이 문제를 풀었는데, dp 를 처음 접했던 문제였던 것 같다.
# DP를 이용해서 풀어보려고 한다. 큰 문제를 작은 거로 만드는 데에 초점을 맞추는 거다.
# 일단 문제를 작게 쪼갤 때 어떤 경우의 수가 나올 수 있는지를 생각했었고,
# [i-1] + 2 라고 생각했었는데, 이거는 그런 문제가 아니라, 경우의 수가 2개로 쪼개지는 것이기 때문에 2 * [i-2] 로 생각을 바꾸었다.
# 마찬가지로 [i-2] * 1이기 때문에 그대로 진행 
# 모듈로 연산은 언제 해도 상관없기 때문에 미리 적용했다.
dp = [0] * (1001)
n = int(input())

dp[0] = 0
dp[1] = 1
dp[2] = 3

for i in range(3, 1001):
    dp[i] = ((dp[i-1] % 10007) + (2 * dp[i - 2]) % 10007) % 10007

print(dp[n])