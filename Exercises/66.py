count = sum = 0
while True:
    num = int(input('Write a Number: (999 to stop)'))
    if num == 999:
        break
    count += 1
    sum += num
print(f'You wrote {count} numbers')
print(f' And the sum is: {sum}')