#묶고 싶었는데, 그것은 zip이 할 수 있다고 한다!
#zip!! 순서와 값을 튜플로 묶을 수 있다.
#튜플은 immutable하므로, 하나의 값만을 바꾸려 할 때 오류가 발생
#이것과 같이 ( , ) 같은 식에서 하나의 요소만 바꾸려고 하면 typeerror발생

#안되겠어서 좀 질문글을 찾아보았는데,
#sorted하고 set이 약간 킥이었다.
#set을 써서 중복된 값을 지워서 같은 인덱스를 갖게 하면 되는구나 싶었고,
#어떻게 해야 dic를 이용해서 시간복잡도를 줄일 수 있을까? 사람들이 계속해서 dic를 쓰면 조회할 때 값이 O(1)이라고 해서
#쓸 방법을 찾다가, dic를 넣었다. index, value값을 넣었는데, 문제는 나는 idnex값을 필요로 하니까,
#어떻게 해야하나 싶었는데, 다양한 방법 중에서 reverse 를 하는 게 어떤가 싶었고
# reverse 후에 get을 해서 문제를 해결할 수 있었다. 
# list를 set으로 해서 중복된 값을 지우고, dictionary 처럼 조회하자는 생각을 했어야 하는 게 제일 중요한 포인트 같다. 


import sys
input = sys.stdin.readline

n = int(input())
string = list(map(int, input().split())) 

arr = sorted(list(set(string))) #여기가 키포인트


dic = dict()
for i in range(len(arr)):
    dic[i] = arr[i]

reverse_dic = {v:k for k, v in dic.items()}

for i in string:
    print(reverse_dic.get(i), end = ' ')