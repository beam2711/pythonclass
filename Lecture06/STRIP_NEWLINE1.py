# This program read the contents of the 
# philosophers.txt file one line at a time.
def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Read three line from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Strip the \n from each string.
    line1 = infile.rstrip('\n')
    line2 = infile.rstrip('\n')
    line3 = infile.rstrip('\n')

    # Close the file.
    infile.close()

    # Print the data thet was read file.
    # memory
    print(line1)
    print(line2)
    print(line3)

# Call the main function.
main()   