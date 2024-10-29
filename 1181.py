#여기서 생각났던 것은 sort, lambda x
#arr.sort(key = lambda x: (기준))으로 배열을 내 마음대로 정렬할 수 있었다.

#파이썬에는 arr.set을 통해서 중복제거가 간단하게 가능하지만 
#for문을 통해서 이전의 값과 비교하여 중복제거를 실시하였다. 
#linked list를 사용해볼까 싶었지만, 파이썬에서 배열을 복사하는 것은 메모리를 낭비하는 행위라고 생각하여 고려하지 않았다. 

n = int(input())
arr = list()

for i in range(n):
    string = input()
    arr.append([string, len(string)])

arr.sort(key=lambda x: (x[1], x[0]))

print(arr[0][0])
for i in range(1, n):
    if arr[i][0] == arr[i-1][0]:
        continue
    else:
        print(arr[i][0])