N = int(input())
P = list(map(int, input().split()))

# 条件より、PはP[i] = 1となるiからiが減少もしくは増加する方向に連番になる
# 先頭の項を末尾に移動させる操作は全体をひっくり返した後に実行すると元の配列の末尾の項を先頭に移動させる操作になる
# 以上より、P[i] = 1となるiを求め、そこから元の配列Pが昇順か降順かを求める。
# 昇順の場合、P = [..., N-2, N-1, 1, 2, ...]なので、P_left=[..., N-2, N-1]とP_right=[1, 2, ...]の部分に分割する。
# P_leftをP_rightの後ろに移動させる場合はlen(P_left)回、移動操作を行う必要がある。
# P_rightをP_leftの前に移動させる場合は1度、反転操作を行い、len(P_right)回、移動操作を行なった後、もう1度,反転操作を行う。

answer = 0

index = P.index(1)

is_ascending = P[(index + 1) % N] == P[index] + 1

if P[(index + 1) % N] == P[index] + 1:
    # ascending, P = ..., 1, 2, ...
    answer = min(index, N - index + 2)
else:
    answer = min(index + 1 + 1, N - (index + 1) + 1)

print(answer)
