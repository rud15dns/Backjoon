#파이썬이니까, 딕셔너리를 이용해보자.
#index : value로 해서 값을 저장하고,
#m개의 줄에서 들어온 값이 문자열이면 index를 찾고,
#숫자면 그에 해당하는 value값을 리턴하면 되겠다. 

#이게 알파벳인지 어떻게 확인해야하지? 알파벳인지 확인하는 함수가 있었던 것 같아서 구글링 -> isalpha
#value값으로 key값을 조회할 때, 일일이 for문을 도는 것보다, 한번에 reverse dict를 만들어서 계산하는 게 더 효율적이겠지? -> reverse_dict

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
pokemon = dict()

for i in range(1, n + 1):
    name = sys.stdin.readline().rstrip()
    pokemon[str(i)] = name

reverse_pokemon = {v:k for k, v in pokemon.items()}

for _ in range(m):
    ask = input()
    
    if ask.isalpha():
        print(reverse_pokemon[ask])
    
    else: #숫자포함이면
        print(pokemon[ask])
