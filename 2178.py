n, m = map(int, input().split())
arr = list()

for i in range(n):
    arr.append(input())

visited = [(0, 0)]
x, y = 0, 0

while (x == n-1 and y == m):
    
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        cx = x + dx
        cy = y + dy

        if (0 <= cx < n and 0 <= cy < m) and arr[cx][cy] == 1:
        