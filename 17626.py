# 어떻게 dp 로 풀어야할지 감이 안옴.

import math

arr = [0] * (50001)
n = int(input())

temp = 0
for i in range(1, 500001):
    if int(math.sqrt(i)) ** 2 == i:
        arr[i] = 1
    else:
