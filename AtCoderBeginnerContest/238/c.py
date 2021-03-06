N = int(input())

# f(x)
# xの桁数を求める。
# 10^(xの桁数 - 1) からxがf(x)の条件を満たす数
# よって、f(x) = x - 10^(xの桁数 - 1) + 1^(xの桁数 - 1) (1桁の時は0を含まないので+1する必要がない)
#
# f(1) +  ... + f(n) + ... + f(N)を求めるには、f(n)を逐次計算するとN < 10^8なので間に合わない。
# f(1), ..., f(n): 1から9の9個の等差数列
# f(10), ..., f(99): 1から90の91個の等差数列
# f(100), ..., f(999): 1から900の901個の等差数列
# ...
# より、各桁のf(n)の総和はO(1)で求められるので、O(log N)で求められる。

digit = len(str(N))

answer = 0
for i in range(digit):
    n = 0
    if i + 1 == digit:
        n = N + 1
    else:
        n = 10 ** (i + 1)

    n -= 10 ** i

    answer += (n * (1 + n) // 2) % 998244353
    # answer += ((n + 1) * (1 + n) // 2) % 998244353

print(answer % 998244353)

# f(90, 1, 90) + f(9, 1, 9) + f(139, 1, 139)
