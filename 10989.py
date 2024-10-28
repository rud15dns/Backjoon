#파이썬은 sort를 통해서 가볍게 구현이 가능하지만, 연습을 위해 quick sort 알고리즘을 이용해볼 것이다. 
'''
arr = list()
for i in range(n):
    arr.append(int(input()))
    arr.sort()

for elem in arr:
    print(elem)
'''
#1000만개의 숫자를 8MB이하로 저장할 수 없다는 문제.


#결국에는 가장 간단하게, pivot보다 작은 거는 왼쪽으로 몰아서 다시 quicksort, pivot보다 큰 것은 오른쪽으로 몰아서 다시 quicksort하는 거라고 생각하면 된다.
'''
def quicksort(low, high):
    if (high > low):
        pivot = partition(low, high)
        quicksort(low, pivot - 1)
        quicksort(pivot + 1, high)
    

#pivot의 위치를 찾아주자.
def partition(low, high):
    pivotitem = arr[low] #첫번째 아이템을 기준으로 삼는다.
    j = low # 바꿀 위치가 될 current ranking (pivot보다 작은 것들이 모일 끝 위치)
    for i in range(low+1, high+1):
        if (arr[i] < pivotitem): #작으면은 pivot의 위치가 더 오른쪽이여야 하므로
            j += 1               #바꿀 위치를 증가시키고, 
            arr[i], arr[j] = arr[j], arr[i]  #작은 것이 내 왼쪽으로 가도록 위치를 변환한다. 

    pivotpoint = j #최종적으로 위치할 pivotpoint
    arr[low], arr[pivotpoint] = arr[pivotpoint], arr[low] #그 최종 위치에 피벗아이템을 넣는다.

    return pivotpoint


# quicksort(0, len(arr)-1)
# for elem in arr:
#     print(elem)
# arr.sort()
# for elem in arr:
#     print(elem)
'''

#현재 문제:메모리초과
#파이썬에서는 arr에서 append하면은 1 <= N <= 10000000 이므로 총 40MB가 필요하다.
#배열을 만들어서 입력된 값을 저장하는 것. -> 시간 초과
#input을 sys.stdin.realine으로 바꾸었음.

#꼭 배열을 만들어서 정렬할 필요 없이, 10000개의 숫자의 개수를 세는 것도 좋은 방법임을 알았다.
import sys

n = int(input())
arr = [0] * 10001

for i in range(n):
    idx = int(sys.stdin.readline())
    arr[idx] += 1

for i in range(10001):
    for j in range(arr[i]):
        print(i)

    
