#스택인데, 사실 파이썬은 스택 구현하기 어렵지 않다고 생각된다. 내 생각에는...
#그냥 구현하려고 했는데, 교과서에서 보았던 class를 이용해보려고 한다. 
#스택에 푸쉬가 안되었었는데, for문 안에 객체를 넣어버려서 계속해서 새로운 객체가 생성되었던 것이다.

#print(1 if stack.isEmpty() else 0) 중요! -> 왜냐하면 파이썬에서는 True를 1로 바로 변환해주지는 않기 때문일것이다. 
#그리고 파이썬의 반복문에서는 input을 쓰지 않는다. 절대로! 시간초과가 난다. 
#대신에 sys.readline().rstrip()을 사용하자.

#두가지 방법으로 풀어보았다. 

import sys
n = int(input())

class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    
    def push(self, X):
        self.top.append(X)
    

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        else:
            return -1
    

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
        else:
            return -1

stack = Stack()

for i in range(n):
    arr = sys.stdin.readline().rstrip().split()
    if arr[0] == "push":
        stack.push(int(arr[1]))

    elif arr[0] == "pop":
        print(stack.pop())

    elif arr[0] == "size":
        print(stack.size())

    elif arr[0] == "empty":
        print(1 if stack.isEmpty() else 0)
    else:
        print(stack.peek())

'''
stack = list()

for i in range(n):
    arr = sys.stdin.readline().rstrip().split()
    if arr[0] == "push":
        stack.append(int(arr[1]))

    elif arr[0] == "pop":
        print(stack.pop(-1) if len(stack)!=0 else -1)

    elif arr[0] == "size":
        print(len(stack))

    elif arr[0] == "empty":
        print(1 if len(stack)== 0 else 0)
    else:
        print(stack[-1] if len(stack) != 0 else -1)
'''
