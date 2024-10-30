# (는 +1, ) 는 -1로 해서 -1이 되면 바로 VPS가 아니게 되고,
# 마지막까지 계산했을 때 0이 아니어도 VPS가 아니다.
# 이렇게 계산하면 괄호를 리스트에 넣지 않아도 되니, 공간을 아낄 수 있을 것이다.

n = int(input())
for i in range(n):
    string = input()
    total = 0
    for elem in string:
        if elem == ")":
            total -= 1
        else:
            total += 1
        
        if total < 0:
            break
    
    if total != 0:
        print("NO")
    else:
        print("YES")

    
    