num = int(input('Write the First Number: '))
ratio = int(input('Write the Ratio: '))
i = 0
while i < 10:
    print(num)
    num += ratio
    i+=1
    if i==10:
        aux= int(input('How many terms do you wanna see? '))
        i -= aux
print('Bye! ')