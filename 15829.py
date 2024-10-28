#브론즈2
'''
FAST CRT란?
중국인의 나머지 정리에서 빠르게 연산할 수 있도록 한 알고리즘으로써,
M = m1 m2 m3 ... mk, 이고 이 때의 m은 서로소 관계이다.
Mi 는 M / mi의 결과이다.

sum = 0
for i in range(1, k + 1):
    ai = A mod mi
    ci = Mi * (Mi^-1 mod mi)
    sum = sum + ai * ci
    if sum >= M then sum = sum - M # 여기서 수를 줄이기 위해서 썼었다.    
'''


def hash(r, M):
    len = int(input()) #문자열의 길이
    string = list(input())
    sum = 0

    for i in range(len):
        a = ord(string[i]) - ord('a') + 1
        # print(a)
        sum += (a * (r ** i)) % M
        # len이 길어질수록, sum의 값이 커지기 때문에 그냥 더하기만 해도 mod M을 해줘야한다.
        # 암호학 시간에 코드에서 봤었다! (fast CRT)
        if sum >= M:
            sum = sum % M

    return sum


r = 31
M = 1234567891

print(hash(r, M))
