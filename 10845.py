'''
저번에 class로 스택을 구현했던 것을 바탕으로 큐를 구현해보자
self.top = [] 처럼 생성자만 잘 생성하면은 그 뒤로는 쉽게 구현할 수 있다.
사실 else 필요없이 return만 사용해도 된다.

반복문에서는 input().split()을 사용하면 안된다는 저번의 교훈에 따라서
sys.stdin.readline()을 이용하였다. 
'''

class Queue:
    def __init__(self):
        self.top = []
    
    def push(self, X):
        self.top.append(X)
    
    def pop(self):
        if self.empty() == 1:
            return -1
        return self.top.pop(0)
    
    def size(self):
        return len(self.top)
    
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    
    def front(self):
        if self.empty() == 1:
            return -1
        else:
            return self.top[0]
    
    def back(self):
        if self.empty() == 1:
            return -1
        else:
            return self.top[-1]

import sys
n = int(input())
queue = Queue()

for i in range(n):
    arr = list(sys.stdin.readline().rstrip().split())
    if arr[0] == "push":
        queue.push(int(arr[1]))
    elif arr[0] == "pop":
        print(queue.pop())
    elif arr[0] == "size":
        print(queue.size())
    elif arr[0] == "empty":
        print(queue.empty())
    elif arr[0] == "front":
        print(queue.front())
    else:
        print(queue.back())