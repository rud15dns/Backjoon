''' square 제곱? 을 실시할 수 있겠다.
    암호학에서 주로 봤던 그 형식말이다!
    Square multiplication!!
'''

a, b, c = map(int, input().split())
tot = 1
while (b > 0):
    if (b & 1):
        tot = (tot * a) 
    a = (a * a) % c
    b = b >> 1

print(tot)