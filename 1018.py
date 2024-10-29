#for문에서 설정을 0, x-8로 해서 반복문이 실행되지 않았다. 지피티가 도움을 주었다..
#그래도 아이디어나 전체적인 모든 코드는 손으로 직접 짰다.
#한 거의 1년간 머리아프게 했던 문제인데, 갑자기 아이디어가 떠올라서 풀 수 있었다.
#못 풀 줄 알았는데, 갑자기 풀려서 당황스럽다.
#배열의 크기가 크지 않기 때문에, 두 가지 패턴 중에서 적게 바꿔야하는 것만 세면 되지 않나? 라는 생각에서 시작했던 것 같다.

arr_W = [[0] * 8 for i in range(8)]
arr_B = [[1] * 8 for i in range(8)]
# print(arr_W)

for i in range(8):
    for j in range(8):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1):
            arr_W[i][j] = 1
            arr_B[i][j] = 0
    

#입력받기
x, y = map(int, input().split())
arr_t = [[0] * y for i in range(x)]

for i in range(x):
    string = input()
    for j in range(y):
        if string[j] == 'W':
            arr_t[i][j] = 1


total = 50 * 50

for i in range(0, x-7):
    for j in range(0, y-7):
        count_W = 0
        count_B = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if arr_W[k-i][l-j] != arr_t[k][l]:
                    count_W += 1
                if arr_B[k-i][l-j] != arr_t[k][l]:
                    count_B += 1
        # print(count_B, count_W)
        tmp = min(count_W, count_B)
        total = min(tmp, total)

print(total)
