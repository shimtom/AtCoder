N, X = [int(x) for x in input().split()]
S = input()

# 二分木の移動をシミュレーションすると頂点の桁数が非常に大きくなりTLEになる。
# 完全二分木のi番目の頂点の深さはfloor(log(i)) + 1なので最悪深さ10^100まで移動することになるが、
# 答えが10^18以下で深さが高々55程度になることが保証されているので、無駄な移動が多く含まれている。
# LまたはRの直後にUが存在する場合、直前のLまたはRの移動は削除できる。
# その為、移動は0個以上のUの後に0個以上のLまたはRが続く文字列に変換することができる。
# すなわち頂点番号は何回か減少した後に何回か増加して最後の頂点になり、
# この文字列をシミュレーションしても頂点はmax(最初にいた頂点、最後にいた頂点)を超えることはないので
# 高速にシミュレーションできる。
# 圧縮O(N)、シミュレーションO(N')

move = []
for s in S:
    if s == 'U' and len(move) > 0 and move[-1] != 'U':
        move.pop()
    else:
        move.append(s)

position = X
for s in move:
    if s == 'U':
        position = position >> 1
    elif s == 'L':
        position = position << 1
    elif s == 'R':
        position = (position << 1) + 1

print(position)
