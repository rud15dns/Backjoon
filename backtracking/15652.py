n, m = map(int, input().split())
seq = list()

def print_num():
    for elem in seq:
        print(elem, end = ' ')
    print()

## n이 고를 수 있는 숫자의 경우
## m이 자리 수
def count(num, start):
    if num > m:
        print_num()
        return

    for select in range(start, n + 1):
        seq.append(select)
        count(num + 1, select)
        seq.pop()

count(1,1)
