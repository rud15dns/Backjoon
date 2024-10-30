'''
이 문제에서 실수했던 것은 0명일 때를 생각하지 않았다는 점과
무작정 빼서 0이 아니면은 tshirt의 개수를 늘렸다는 점이다.

간단하게 나눗셈과 나머지를 이용하면은 몇 묶음을 살 수 있는지 알 수 있었는데 말이다.
초등학교 개념도 까먹은 게 아닐까? 싶다.

몇 묶음이 나오고, 나머지 계산을 하였다.
'''

n = int(input())
arr = list(map(int, input().split()))
t, p = map(int, input().split())

tshirt = 0

# 티셔츠 장수 계산
for i in range(6):
    if arr[i] == 0:
        continue

    tshirt += arr[i] // t

    if arr[i] % t > 0:
        tshirt += ((arr[i] % t) // t + 1)

print(tshirt)
print(n // p, n % p)