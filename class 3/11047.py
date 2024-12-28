#뒤에서부터 빼면 될듯하다.
#0이 되기전까지
#시간초과가 발생함. 
#나눗셈은 어떤가? -> 정답!
#다른 사람의 코드에서는 반복문을 단일로 계속 반복하라고 했었는데, 그 코드 가운데에서 나눗셈을 발견했고,
#그순간 나눗셈의 몫과 나머지의 큰 역할이 떠오르면서 계산을 확 줄일 수 있겠다는 생각이 들었다.
#이전의 경우에서는 나쁜 경우에는 O(n^2)의 시간복잡도를 가질 수 있었는데, 
#몫과 나머지를 이용해서 계산의 크기를 확 줄인 결과 O(n)의 시간복잡도를 가질 수 있었다.

#+) 어제 포켓몬스터 문제 시간복잡도 계산에서, dict를 만들 때 n번, 답변 출력할 때, dict를 접근하는 횟수가 m번이라 O(m + 2n)이냐고 질문을 남겼었는데,
#dict 접근할 때, isalpha라는 함수를 사용하는데, 이 함수가 문자열의 길이 만큼의 시간복잡도를 가지기 때문에, O(n + mk)의 시간복잡도를 가진다고 이야기해주셨다.

'''
   if tmp - node >= 0:
        # print("node", node)
        while tmp >= 0:
            tmp = tmp - node
            cnt += 1
            # print(tmp)
        tmp = tmp + node
        cnt -= 1
'''
import sys

n, k = map(int, input().split())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt = 0

for _ in range(n):
    if k == 0:
        break

    node = arr[n - _ - 1]

    cnt += k // node
    k = k % node
    
    # print("k", k, "cnt", cnt)

print(cnt)