N, K = [int(x) for x in input().split()]

# 一つ目のボールの塗り方はK通り
# 二つ目のボールの塗り方は、一つ目で使用した色以外を使用できるのでK - 1通り
# 三つ目のボールの塗り方は、二つ目で使用した色以外を使用できるのでK - 1通り
# まとめると、K x (K - 1) ^ (N - 1)通り
print(K * (K - 1) ** (N - 1))