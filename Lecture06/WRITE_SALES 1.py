# This program the user for sales amoumt
# and writes those amounts to sales.txt file
def main():
    # Get the numbre of days.
    num_days = int(input('For how many days do ' + \
                         'you have sales? '))
    # Open a new file named sales.txt.
    sales_file = open('sales,txt', 'w')

    # Get the amount of sales for each day and write
    # it to the file.
    for count in range(1, num_days + 1):
        sales = float(input('Enter the sales for dat #' + \
                            str(count) + ': '))
        # Get the sales for a day.
        sales_file.write(str(sales) + '\n')

    # Close the file.
    sales_file.close()
    print('Data written to sales.txt.')

# Call the main function.
main()