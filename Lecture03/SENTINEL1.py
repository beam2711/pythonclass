products = 'y'

while products == 'y':
    sales = float(input("Enter the item's wholesale cost: "))
    commission = sales * 2.5
    
print('The commission is $', \
    format(commission, ',.2f'),sep='')

products = input('Do you want to calculate another' + \
                       'commission (Enter y for yes)')