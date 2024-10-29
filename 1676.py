#파이썬은 string으로 바꾸면 배열로다가 사용할 수 있다는 생각을 이용하였다.
#factorial 함수를 for문으로 만들고, int(a[i])를 비교하면서 뒤에서부터 0의 개수를 세었다.

def facto(n):
    r = 1
    for i in range(n, 1, -1):
        r *= i
    
    return r

a = str(facto(int(input())))
count = 0
for i in range(len(a)-1, 0, -1):
    # print(a[i])
    if int(a[i]) == 0:
        count += 1
    else:
        break

print(count)