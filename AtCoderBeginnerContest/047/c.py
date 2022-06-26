S = input()

answer = 0
current = None
for i, s in enumerate(S):
    if current is None:
        current = s
    if current != s:
        answer += 1
        current = s
print(answer)
