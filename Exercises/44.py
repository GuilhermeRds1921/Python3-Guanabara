store = float(input('How much is it? '))
method =int(input('''forms of payment
[ 1 ] In cash (10% discount): 
[ 2 ] x1 in credit card (5% discount):
[ 3 ] x2 in credit card (interest-free):
[ 4 ] x3 or more in credit card(20% interest): 
Chose one method: '''))
if method == 1:
    print('Will cost: R${:.2f}'.format(store-(store*0.1)))
elif method == 2:
    print('Will cost: R${:.2f}'.format(store-(store*0.05)))
elif method == 3:
    print('Will cost: R${:.2f}'.format(store))
elif method == 4:
    print('Will cost: R${:.2f}'.format(store+(store*0.2)))
else:
    print('This an invalid option! ')