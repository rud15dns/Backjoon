# 처음에는 0 * 4 ^ N + func(N - 1, i, j)로 생각했었는데, else: 를 return으로 받는 게 아니고, base도 그냥 할당에 머물러있고,
# 4개가 동시에 진행되고 있어서
# 뒤에 더한 게 의미가 없어졌음. 그래서 score라는 변수를 따로 만들어서 같이 넘겨주었다. 
# 메모리 초과당함. 아무리봐도 음... 재귀를 사용함으로써 깊어지고, 여러 개를 동시다발적으로 해서 그런 것 같다.
# 저장할 arr 이 필요한가?

N, c, r = map(int, input().split())

x, y = 0, 0
i = 1
score = 0

for i in range(1, N + 1):
    if x == c and y == r:
        break
    
    size = 2 ** (N - i)    

    if c < x + size and r < y + size:
        score = score

    elif c < x + size and r >= y + size:
        score = score + 1 * (4 ** (N - i))
        y = y + size

    elif c >= x + size and r < y + size:
        score = score + 2 * (4 ** (N - i))
        x = x + size

    else:
        score = score + 3 * (4 ** (N - i))
        x = x + size
        y = y + size 

print(score)


# 이 코드도 된다. 안되가지고 메모리 초과나서 진짜 너무 슬펐는데
# 사실 별건 아니었고, arr을 맨 처음에 한 게 너무 커서 그랬던 거다. 
# 덕분에 4분면을 이용하는 방법하고, 반복문으로도 하는 방법을 claud 하고 토론했으니까 된건가 ? 

# def func(N, i, j, score):
    
#     size = 2 ** (N - 1)
#     if i == c and j == r:
#         return score

    
#     if i == c and j == r:
#         return score 
    
#     else:
#         size = 2 ** (N - 1)

#         if c < i + size and r < j + size:
#             return func(N-1, i, j, score)
        
#         elif c < i + size and r >= j + size:
#             return func(N-1, i, j + size, score + 1 * (4 ** (N-1)))
        
#         elif c >= i + size and r < j + size:
#             return func(N-1, i+size, j, score + 2 * (4 ** (N-1)))
        
#         else:
#             return func(N-1, i+size, j+size, score + 3 * (4 ** (N-1)))

# print(func(N, 0, 0, 0))