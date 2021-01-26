num = 0
count = 0
sum = 0
while num != 999:
    num = int(input('Write a Number: '))
    sum += num
    count += 1
print('Foram mostrados {} '.format(count - 1))
print('E a soma foi {}'.format(sum - 999))