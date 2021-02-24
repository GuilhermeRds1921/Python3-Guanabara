while True:
    num = int(input('\nChoose a Number to see the multiplication table(>0): '))
    print('='*20)
    if num <= 0:
        break
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')
    print('=' * 20)
print('Bye! ')
