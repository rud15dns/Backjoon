# 스택 쌓는 것처럼 생각했다.
# 반을 기준으로 스택을 쌓고, 스택을 꺼내면서 현재의 것과 비교하는 느낌으로.

while True:
    a = input()
    if (int(a) == 0):
        break
    N = len(a)
    for i in range(0, N//2):
        if (int(a[i]) != int(a[N-1-i])):
            print("no")
            break
    else:
        print("yes")
    