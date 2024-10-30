#직접 종이에 하나씩 쓰다보니까, 규칙이 나왔다.
#그냥 점화식 풀듯이 하나씩 쓰다보니 되었다.

n, k = map(int, input().split())

arr = list()
for i in range(1, n+1):
    arr.append(i)

prev = 0
print("<", end = '')
for i in range(n):
    output = (prev + k - 1) % len(arr)
    if (i == n-1):
        print(arr[output], end = '>')
    else:
        print(arr[output], end = ', ')

    prev = output
    arr.pop(output)
