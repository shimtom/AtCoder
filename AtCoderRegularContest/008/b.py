import math
import sys

N, M = map(int, input().split())
name = input()
kit = input()

name_chars = dict()
for c in name:
    name_chars[c] = name_chars.get(c, 0) + 1

kit_chars = dict()
for c in kit:
    kit_chars[c] = kit_chars.get(c, 0) + 1

answer = -1
for c, n in name_chars.items():
    if c not in kit_chars:
        print(-1)
        sys.exit()
    else:
        answer = max(answer, int(math.ceil(n / kit_chars[c])))

print(answer)
