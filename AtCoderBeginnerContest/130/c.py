import math

W, H, X, Y = [int(x) for x in input().split()]

# 与えられた点と対角線の交点を通る直線で分割した時に面積を二等分するので
# 分割された小さい方の面積の最大値は長方形の面積の1/2。
#
# 二等分する直線が複数引けるのは、与えられた点が対角線の交点と一致するとき。

max_area = W * H / 2
is_intersection = math.isclose(X, W / 2, abs_tol=10**-9) and math.isclose(
    Y, H / 2, abs_tol=10**-9
)

print(max_area, int(is_intersection))
