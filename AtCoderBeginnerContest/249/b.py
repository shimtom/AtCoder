S = input()

if not S.isupper() and not S.islower() and len(S) == len(set(S)):
    print('Yes')
else:
    print('No')
