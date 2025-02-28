n = int(input())
cnt = 0

cols = [False] * n           # 같은 열에 퀸이 있는지 확인
diag1 = [False] * (2 * n - 1)  # 가능한 대각선 길이의 개수
diag2 = [False] * (2 * n - 1) 

def queen(row):
    global cnt
    if row == n:  # 모든 행에 퀸이 배치되면 통과
        cnt += 1
        return
    
    for col in range(n):
        if not cols[col] and not diag1[row + col] and not diag2[row-col+(n-1)]:
            #위아래, 대각선 모두 안놓여져있으면
            cols[col] = True
            diag1[row + col] = True
            diag2[row-col+(n-1)] = True

            #다음 행으로 이동
            queen(row + 1)

            #백트래킹: 복구
            cols[col] = False
            diag1[row + col] = False
            diag2[row-col+(n-1)] = False


queen(0)
print(cnt)
