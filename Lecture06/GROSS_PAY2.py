# This program calculates gross pay.

def main():
    try:
        # Get the number fo hours worked.
        hours = int(input('How many hours did you work? '))

        # Get the hourly pay rate.
        pay_rate = float(input('Enter your horly pay rate: '))

        # Calculate the pay gross pay.
        gross_pay = hours * pay_rate

        # Display the gross pay.
        print('Gross pay: $', format(gross_pay,',.2f'), sep='')
    except ValueError:
        print('ERROR: Hours worked and hourly pay rate musst')
        print('be valid integers.')

# Call the main funtion.
main()