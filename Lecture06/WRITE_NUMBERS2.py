# This progeam demonstrates how numbers
# musbe coverted to strings before they
# are written to a text file

def main():
    # Open a file for writing.
    outfile = open('numbers.txt', 'w')

    # Get three numbers from the user.
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter another number: '))

    # Write the numbers to the user.
    outfile.weite(str(num1) + '\n')
    outfile.weite(str(num2) + '\n')
    outfile.weite(str(num3) + '\n')

    # Close the file.
    outfile.close()
    print('Data written to numbers.txt')
# Call the main function.
main()