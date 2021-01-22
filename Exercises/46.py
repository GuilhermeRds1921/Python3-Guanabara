from time import sleep
print('='*17)
print('|\tcountdown\t|')
print('='*17)
sec = 10
for i in range(0, 11):
    print(sec)
    sleep(1)
    sec -= 1
print('BOM!!!')