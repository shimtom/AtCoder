L, X, Y, S, D = map(int, input().split())

# SからDの距離を時計回り、反時計周りそれぞれで求め、
# 各距離について、時計回り、反時計回りに移動した場合の時間を求める
#
# ただし、反時計回りに移動するときは床の時計回りの移動速度Xより、
# 移動速度Yが大きくないと反時計回りに移動できないので注意

if D > S:
    d_cw = D - S
    d_ccw = L - d_cw
else:
    d_ccw = S - D
    d_cw = L - d_ccw
v_cw = X + Y
v_ccw = - (X - Y)
if v_ccw > 0:
    answer = min(d_cw / v_cw, d_ccw / v_ccw)
else:
    answer = d_cw / v_cw

print(answer)
