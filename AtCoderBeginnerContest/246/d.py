N = int(input())


# f(a, b) = a^3 + a^2b + ab^2 + b^3
#         = (a + b)(a^2 + b^2)
# a^2 + b^2 = (a + b)^2 - 2ab
def f(a, b):
    return (a + b) * ( a ** 2 + b ** 2)

# O(n) two pointers
a = 0
b = 10 ** 6
answer = 10 ** 18 + 1
while a <= b:
    x = f(a, b)
    if x >= N:
        answer = min(answer, x)
        b -= 1
    else:
        a += 1


# O(n log(n)) (n <= 10 ** 6) binary tree search
# answer = 10 ** 18 + 1
# for a in range(10 ** 6):
#     b_left, b_right = a-1, 10 ** 6

#     while b_right - b_left > 1:
#         b_middle = (b_left + b_right) // 2
#         if f(a, b_middle) >= N:
#             b_right = b_middle
#         else:
#             b_left = b_middle

#     if a > b_right:
#         break

#     answer = min(answer, f(a, b_right))

print(answer)
