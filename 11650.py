#똑같이 lambda 쓰면 되지 않을까? 싶다
n = int(input())
arr_2 = list()
for i in range(n):
    arr = list(map(int, input().split()))
    arr_2.append(arr)
arr_2.sort(key=lambda x: (x[0], x[1]))

for elem in arr_2:
    print(elem[0], elem[1])
