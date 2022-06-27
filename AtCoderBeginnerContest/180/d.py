import math
X, Y, A, B = map(int, input().split())

# 全探索は無理 O(2^MAX_EXP)
#
# ジムの通い方はいくつかのパターンが考えられる。
# カコモンジムに通う回数をa, AtCoderジムに通う回数をb
# 最後に纏めて行く場合の強さ:
#   X*A^a + B*b
# 途中に何回か挟む場合、例えば:
#   (X*A^a1 + B*b1)*A^a2 + B*b2
# = X*A^(a1 + a2) + B*b1*A^a2 + B*b2
# = X*A^(a1 + a2) + B(b1*A^a2 + b2)
# = X*A^a + B*b, (a=a1+a2, b=b1*A^a2 + b2)
# 以上より、どのような通い方をしても強さは X*A^a + B*b の形で表すことができる。
# よって、X*A^a + B*b < Yでa + bが最大となるa,bを求めればよい

# avoid X*A^a + B*b == Y
Y -= 1


def f(a, b):
    return X * A ** a + b * B


def g(a):
    b = (Y - X * A ** a) // B
    return b


def h(b):
    a = int((math.log(Y - b * B) - math.log(X)) / math.log(A))
    return a


max_exp = 0
b_left = 0
b_right = g(0)
while b_left + 1 < b_right:
    b_middle = (b_right + b_left) // 2

    a_left = h(b_left)
    a_right = h(b_right)
    a_middle = h(b_middle)

    exp_left = a_left + b_left
    exp_right = a_right + b_right
    exp_middle = a_middle + b_middle

    if exp_right > exp_left:
        b_left = b_middle
    else:
        b_right = b_middle

b = b_right
a = h(b)

print(a + b)
