N = int(input())

Ss = [-1 for _ in range(18)]

def string(index):
    """S_{n - 1}, n, S_{n - 1}"""
    if index == 1:
        return '1'

    if Ss[index - 1] == -1:
        Ss[index - 1] = string(index - 1)

    ans = Ss[index - 1] + ' ' + str(index) + ' ' + Ss[index - 1]

    return ans

print(string(N))
