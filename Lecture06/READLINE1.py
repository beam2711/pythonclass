# This program reads the contents of the
# philosophers.txt file one line at a time.
def main():
    # Open a file named philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Read three lines from the file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Print the data thet was read file.
    # memory
    infile.close()
    print(line1)
    print(line2)
    print(line3)

# Call the main function.
main()