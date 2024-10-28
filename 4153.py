#직각삼각형인지 판단하기 위해서는, 가장 긴 변의 길이를 찾는 게 우선이겠다.
#배열로 int타입으로 받아서, sort한 후에 첫 번째에 위치한 수를 잡으면 되겠다.

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break

    arr.sort(reverse=True)
    if (arr[1] ** 2) + (arr[2] ** 2) == (arr[0] ** 2):
        print("right")
    else:
        print("wrong")
