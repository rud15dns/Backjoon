'''
gcd(a, b) = gcd(b, a % b) = ....
a * b = 최대공약수 * 최소공배수
b가 0일 때, 그 때의 a가 최대공약수이다.
'''
def gcd(a, b):
    while (b != 0):
        tmp = b
        b = a % b
        a = tmp
    
    return a


n1, n2 = map(int, input().split())
print(gcd(n1, n2))
print((n1 * n2) // gcd(n1, n2))