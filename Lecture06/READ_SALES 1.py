def main():
    # Open the sales.txt file for reading.
    sales_file = open('sales.txt', 'r')

    # Read the first line from the , but
    # don't convert to a numbre tey. We still
    # need to test for an emty string.
    line = sales_file.readline()
    
    # As long as an empty string is not returned
    # from readline, continme processing.
    while line != '':
        # Convert line to a float.
        amount = float(line)

        # Format and display the amount.
        print(format(amount, '.2f'))

        # Read the next line
        line = sales_file.readline()
    
    # Close the file.
    sales_file.close()

# Call the main function.
main()