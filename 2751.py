#수 정렬하기 3에서 실시했던 것과 같은 방법을 사용할 수 있을 것 같지만,
#메모리 제한이 없기 때문에 quick정렬을 복기해보고자 사용해본다.
#퀵 정렬에서 pivot을 첫번째로 설정했을 경우, 최악의 경우 O(n^2)이므로, pivot을 무작위로 생성한다
#그런 의미에서 퀵 정렬은 어떠한 문제에서도 사용하지 않는 게 좋다고 한다. 
#차라리 병합 정렬을 사용하는 편이 낫다. O(NlogN) 이하의 복잡도를 가지기 때문이다.
#언젠가 다시 볼테니 그때보면 다시 복습하는 느낌으로 지금은 개념을 잡아두고 간다. 
import sys
n = int(input())
arr = list()
sorted = [0] * (100 * 10000)
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)

def merge(arr, left, mid, right):
    global sorted
    k = left
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            sorted[k] = arr[i]
            i, k = i+1, k+1
        else:
            sorted[k] = arr[j]
            j, k = j+1, k+1
    
    if i > mid:
        sorted[k:k+right-j+1] = arr[j:right+1]
    else:
        sorted[k:k+mid-i+1] = arr[i:mid+1]
    arr[left:right+1] = sorted[left:right+1]

merge_sort(arr, 0, len(arr) - 1)
for elem in arr:
    print(elem)



# def partition(low, high):
#     pivotitem = arr[low]
#     j = low
#     for i in range(low+1, high+1):
#         if (pivotitem >= 0 and arr[i] < pivotitem):
#             j += 1
#             arr[i], arr[j] = arr[j], arr[i]
#         elif (pivotitem < 0 and abs(arr[i]) > abs(pivotitem)):
#             j += 1
#             arr[i], arr[j] = arr[j], arr[i]

        

#     pivotpoint = j
#     arr[low], arr[pivotpoint] = arr[pivotpoint], arr[low]

#     return pivotpoint


# def quicksort(left, right):
#     if (right>left):
#         pivot = partition(left, right)
#         quicksort(left, pivot - 1)
#         quicksort(pivot+1, right)

# quicksort(0, len(arr)-1)

# for elem in arr:
#     print(elem)

