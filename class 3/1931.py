import sys
input = sys.stdin.readline

n = int(input())
time = []

for _ in range(n):
    x, y = map(int, input().split())
    time.append((x, y))

time.sort(key=lambda x: (x[1], x[0]))
print(time)
cnt = 0

for start_time, end_time in time:
    if cnt == 0:
        prev_time = end_time
        cnt += 1

    elif prev_time <= start_time:
        prev_time = end_time
        cnt += 1

    print(start_time, end_time, prev_time, cnt)

print(cnt)
