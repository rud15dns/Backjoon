# 1 1 1 2 2 까지는 기본으로 만들어두고, 3부터 2 + arr[i] 해서 i가 0인 거부터 하면 되겠는데
# 직접 써보니까, 약간의 규칙이 있더라... 수열로 생각하니까, 이게 전의 꺼에 또 붙이고 붙이는 느낌이라서
# 연역법으로 했더니 되었다.

# 이전의 값을 저장하여 현재의 값으로 사용했으니 Dynamic Programming이라고 볼 수 있겠다.
# 내가 생각했던 개념은 점화식에 가까웠는데, 사실 점화식과 DP가 일맥상통하는 부분인 게 아닐까?
import sys

t = int(input())
arr = [0] * (101)
arr[1] = 1
arr[2] = 1
arr[3] = 1
arr[4] = 2 
arr[5] = 2

def wave():
    for i in range(6, 101):
        arr[i] = arr[i-1] + arr[i-5]
        # print("arr[", i, "] = ", arr[i])

wave()

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(arr[n])

