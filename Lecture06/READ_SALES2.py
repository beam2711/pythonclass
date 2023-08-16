# This program uses the for loop to read
# all of the values in the sales.txt file.

def main():
    # Open the sales.txt file foe reading.
    sales_file = open('sales.txt', 'r')
    # Read all the line from the file.
    for line in sales_file:
        #Convert line to a float.
        amount = float(line)
        # For and display the amount.
        print(format(amount, '.2f'))

    # Close the file.
    sales_file.close()

# Call the main function.
main()