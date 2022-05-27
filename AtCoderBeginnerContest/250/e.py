from pickle import TRUE


N = int(input())
A = [int(a) for a in input().split()]
B = [int(b) for b in input().split()]
Q = int(input())

Queries = []
for _ in range(Q):
    x, y = input().split()
    Queries.append((int(x), int(y)))

indices = []
A_set, B_set = set(), set()

# A: 1 2 3 4 5
# B: 1 2 2 4 3

# A: 1 2 3 4 5 6
# B: 1 2 2 4 2 3
# 中身が同じ2つのsetがあります。
# 1. 次の要素を追加しても同じですか？
#   YES: Aの要素を追加してもsetが不変なので同じです。
#   YES: Bの要素を追加してもsetが不変なので同じです。
#   YES: Aの要素 = Bの要素なので両方追加すれば同じです。
#   No: Aの要素 != Bの要素でどちらもsetにないので、追加すれば異なります。
# 中身が異なる2つのsetがあります。
# 次の要素を追加すれば同じになりますか？
same_set = set()
i, j = 0, 0
while i < len(A) or j < len(B):
    if i < len(A) and A[i] in same_set:
        i += 1
        indices.append((i, j))
    elif j < len(B) and B[j] in same_set:
        j += 1
        indices.append((i, j))
    elif i < len(A) and j < len(B) and A[i] == B[i]:
        same_set.add(A[i])
        i += 1
        j += 1
        indices.append((i, j))
    else:
        A_set, B_set = set(), set()
        while i < len(A) or j < len(B):
            if i <= len(A) and A[i] in same_set:
                i += 1
            elif j < len(B) and B[j] in same_set:
                j += 1
            elif i < len(A) and A[i] in A_set:
                i += 1
            elif j < len(B) and B[j] in B_set:
                j += 1
            elif len(A_set) > 0 and len(B_set) > 0 and A_set == B_set:
                same_set.update(A_set)
                indices.append((i, j))
                break
            elif len(A_set) < len(B_set):
                A_set.add(A[i])
                i += 1
            elif len(A_set) > len(B_set):
                B_set.add(B[j])
                j += 1
            else:
                if i < len(A):
                    A_set.add(A[i])
                    i += 1
                elif j < len(B):
                    B_set.add(B[j])
                    j += 1



# i: ^
# j:
# i: ^
# j: ^
# i:   ^
# j:   ^
# i:   ^
# j:     ^
# i:     ^
# j:     ^
# i: ^ 1
# j: ^ 1
# i:   ^ 2
# j:     ^ 2-3
# i:        ^ 4
# j:          ^ 5
# (1, 1), (2, 2), (2, 3), (4, 5)
# indices = []
# A_set, B_set = set(), set()

# i, j = 0, 0
# while i < len(A) or j < len(B):
#     # both new items equals
#     if i < len(A) and j < len(B):
#         if A[i] == B[j] and A[i] not in A_set and B[j] not in B_set:
#             A_set.add(i)
#             B_set.add(j)
#             indices.append((i, j))
#         i += 1
#         j += 1
#     else:

#         # setが変わるまでindexを進める
#         while i < len(A) and A[i] in A_set:
#             indices.append((i, j))
#             i += 1
#         while j < len(B) and B[j] in B_set:
#             indices.append((i, j))
#             j += 1


#     # サイズか内容が異なるときはindexを進める



#     if len(A_set) == len(B_set):
#         # setが変わるまでindexを進める
#         while i < len(A) and A[i] in A_set:
#             indices.append((i, j))
#             i += 1
#         while j < len(B) and B[j] in B_set:
#             indices.append((i, j))
#             j += 1

#         # both set changing
#         # both new item equal
#         if i < len(A) and j < len(B) and A[i] == B[j]:
#             A_set.add(A[i])
#             B_set.add(B[i])
#             indices.append((i, j))
#             i += 1
#             j += 1
#         # add to one set
#         else:
#             if i < len(A):
#                 i += 1


#     # both set changing
#     # both set equal
#     while A_set != B_set:

#         if i + 1 < len(A) and j + 1 < len(B) and A[i + 1] == B[j + 1]:
#             i += 1
#             j += 1
#         else:


#         # one set changing
#         if i + 1 < len(A):
#             i += 1
#         else:
#             j += 1


# while i < len(A) or j < len(B):
#     if len(A_set) < len(B_set):
#         if i < len(A):
#             i += 1
#     elif len(A_set) > len(B_set):
#         if j < len(B):
#             j += 1
#     else:
#         while i < len(A) and A[i] in A_set:
#             indices.append((i, j))
#             i += 1
#         while j < len(B) and B[j] in B_set:
#             indices.append((i, j))
#             j += 1
#         if i + 1 < len(A) and j + 1 < len(B) and A[i + 1] == B[j + 1]:
#             if i < len(A):
#                 i += 1
#             if j < len(B):
#                 j += 1
#         else:
#             if i < len(A):
#                 i += 1
#             elif j < len(B):
#                 j += 1
#             else:
#                 break

for x, y in Queries:
    if (x, y ) in indices:
        print('Yes')
    else:
        print('No')

# print(indices)

# uniqueで作れる最大のIndexを求める。
# こんな感じのテーブルを作ればいい？
# B \ A: 1
# 1    : T T T T
# A \ B: 1 2 3
# 1    : F F
# 2    : T F
# 3


# O(QN)
# for x, y in Queries:
#     if set(A[:x]) == set(B[:y]):
#         print('Yes')
#     else:
#         print('No')
