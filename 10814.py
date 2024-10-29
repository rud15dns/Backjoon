n = int(input())
arr = list()

for i in range(n):
    a = list(map(str, input().split()))
    arr.append(a)

arr.sort(key=lambda x: (int(x[0])))

for elem in arr:
    print(elem[0], elem[1])