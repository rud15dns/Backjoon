## 백트래킹 연습
n, s = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0


def count(자리수, 현재, 시작점):
    global ans
    if 현재 > 자리수:
        # print(자리수, total, ans)
        if sum(total) == s:
            ans += 1
        return
    
    for i in range(시작점, n):
        total.append(arr[i])
        count(자리수, 현재 + 1, i + 1)
        total.pop()


for i in range(n):
    total = []
    count(i, 0, 0)

print(ans)
