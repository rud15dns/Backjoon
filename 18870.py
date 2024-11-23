#묶고 싶었는데, 그것은 zip이 할 수 있다고 한다!
#zip!! 순서와 값을 튜플로 묶을 수 있다.
#튜플은 immutable하므로, 하나의 값만을 바꾸려 할 때 오류가 발생
#이것과 같이 ( , ) 같은 식에서 하나의 요소만 바꾸려고 하면 typeerror발생


n = int(input())
arr = list(map(int, input().split()))
arr_idx = [i for i in range(n)]

paired = list(zip(arr, arr_idx))
paired.sort(key=lambda x: x[0])

arr_2 = list()
for i in range(n):
    cnt = 0
    idx = i

    for j in range(i-1, -1, -1):
        if paired[j][0] != paired[i][0] and paired[j][0] != paired[idx][0]:
            cnt += 1
        idx = j

    arr_2.append([cnt , paired[i][1]])


arr_2.sort(key=lambda x: x[1])

for elem, idx in arr_2:
    print(elem, end = ' ')