# 최솟값이니까, 생각해보면, -가 처음 나온 시점부터 계속해서 다 빼버리면 되는 부분이었다.
# re.split을 이용하면 구분자를 여러 개 포함할 수 있는데, 나는 -가 처음 나온 시점이 궁금하였기 때문에,
# 구분자를 꼭 포함시켜야 했다.
# 그러기 위해서는 괄호를 포함시키면 되었다. r'([+-])'처럼
# 만약 괄호를 포함시키고 싶지 않다면, r'[]' 라고 쓰면 된다.


import re
minus = False

full =  input()
temp = re.split(r'([+-])', full)
total = 0


for elem in temp:
    if elem == '-':
        minus = True

    if elem != '-' and elem != '+':
        if minus == True:
            total -= int(elem)
        else:
            total += int(elem)

print(total)