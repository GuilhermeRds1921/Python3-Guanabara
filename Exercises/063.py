

num = int(input('How many terms do you wanna see? '))
i = 1
j = 0
a = 0
while num != 0:
    print('{} '.format(i), end = '')
    i += j
    j = i - a
    a = j
    num -= 1