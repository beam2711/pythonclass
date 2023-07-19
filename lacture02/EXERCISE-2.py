hours = int(input('What is your hours worked? '))
rate = float(input('What is your hourly pay rate? '))
if hours <= 40:
    print('Your gross pay is: $',format(hours*rate, '.2f'))
else:
    print('Your gross pay is: $',format(40*rate+(hours-40)*1.5*rate, '.2f'))