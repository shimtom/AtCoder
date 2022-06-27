N, L = [int(x) for x in input().split()]
S = []
for _ in range(N):
    S.append(input())

# 全通り試すのはO(N! * NL)で現実的ではない。

def compare(s, t):
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            break
    else:
        return len(s) < len(t)

    for i in range(min(len(s), len(t))):
        for j in range(i):
            if not (s[j] == t[j] and s[i] < t[i]):
                return False

    return True

for i in range(N):
    for j in range(N):
        if i != j:
            print(S[i], S[j], compare(S[i], S[j]))
