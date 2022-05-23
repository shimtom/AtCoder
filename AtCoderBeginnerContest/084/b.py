A, B = [int(x) for x in input().split()]
S = input()

code = S.split('-')
if len(code) == 2 and '-' not in code[0] and '-' not in code[1] and len(code[0]) == A and len(code[1]) == B:
    print('Yes')
else:
    print('No')
