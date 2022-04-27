A, B, C, D, E, F, X = [int(x) for x in input().split()]

T1, T2 = X, X
takahashi, aoki = 0, 0

while T1 >= 0:
    takahashi += B * min(T1, A)
    T1 -= (A + C)

while T2 >= 0:
    aoki += E * min(T2, D)
    T2 -= (D + F)

if takahashi > aoki:
    print('Takahashi')
elif takahashi < aoki:
    print('Aoki')
else:
    print('Draw')
