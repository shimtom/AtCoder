import sys

N = int(input())

if N % 2 != 0:
    sys.exit()

strings_list = [[] for _ in range(N // 2)]
for n in range(N // 2):
    if n == 0:
        # strings = [['(', ')']]
        strings = ['()']
    else:
        strings = []

        # add ( + S + )
        for s in strings_list[n - 1]:
            # strings.append(['('] + s + [')'])
            strings.append('(' + s + ')')

        # add S + T, T + S
        for i in range(n):
            for s in strings_list[i]:
                for t in strings_list[n - i - 1]:
                    string = s + t
                    # if string not in strings:
                    strings.append(string)

        # strings = sorted(strings)
        new_strings = []
        before_s = ''
        for s in sorted(strings):
            if s != before_s:
                new_strings.append(s)
                before_s = s
        strings = new_strings

    strings_list[n] = strings

for s in strings_list[-1]:
    print(s)
