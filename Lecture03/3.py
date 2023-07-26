#This progeam calculates commissions.
 #Create a variable to control the loop.
keep_going = 'y'

#Create a series fo commissions.
while keep_going == 'y':
    sales = float(input('Enter the amoun of sales: '))
    comm_rate = float(input('Emter the commissions rate: '))

    commission = sales * comm_rate 

    print('The commission is $', \
    format(commission, ',.2f'),sep='')

    keep_going = input('Do you want to calculate another' + \
                       'commission (Enter y for yes)')