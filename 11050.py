'''
이항계수 nCk = 원하는 개수만큼 뽑는 조합의 가짓수
nCk = n! / ((n-k)!*k!)
'''

def facto(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    
    return r


n, k = map(int, input().split())
print(int(facto(n) / (facto(n - k) * facto(k))))
