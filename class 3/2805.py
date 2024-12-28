#배열에 저장한 후에, min값으로 빼서 그 합이 원하는 것보다 크면 더 빼고, 작으면은 더 더하는 형식으로 풀어야겠다.
#답은 맞는데, 시간 초과 발생 -> 이진 탐색에 대해서 알아보자.
#피봇에 대해서 이진 탐색을 해보면 되려나
#정확히 m미터의 나무를 가져가는 게 불가능할 수 있다.
#일단 piv을 프린트문으로 설정해서 오류가 나는 것으로 판명되었다.
#다만 2 15 5 10 이라는 테스트 케이스에서는 지금 제대로 된 값이 나오지 않는 것 같은데, 라고 생각했는데, 제대로 출력하고 있었다.
#pypy 로 제출했더니 시간복잡도 문제를 해결하긴 했다.
#이 문제에서는 시간 복잡도가 low + high에서 //2 가 되므로 log_2n에다가 모든 요소에 대해서 도니까 O(nlogm)이 되겠다.
#어렵다 진짜
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list( map(int, sys.stdin.readline().rstrip().split()))

low = 0
high = max(arr)

while low <= high:

    tot = 0
    piv = (low + high) // 2

    for i in range(len(arr)):
        
        ab = arr[i] - piv
        if ab < 0:
            ab = 0
            
        tot += ab

    
    if tot >= m:
        low = piv + 1
    else:
        high = piv - 1
    
    print("piv", piv, "low", low, "high", high, "tot-m", tot-m, "tot", tot)
    
   

print(high)