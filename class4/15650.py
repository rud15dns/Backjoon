n, m = map(int, input().split())

answer = []


def print_num():
    for elem in answer:
        print(elem, end = ' ')
    print()

## m자리, 선택해야 할 수는 1~n까지
def foo(num, start):
    if num >= m + 1:
        print_num()
        return

    for select in range(start, n + 1):
        answer.append(select)
        foo(num + 1, select + 1)
        answer.pop()

    return

foo(1, 1)