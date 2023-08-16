# This progran writes three lines of sata
# to a file
def main():
    # Open a file named philosophers.txt. 
    outfile = open('philosophers.txt' , 'w')

    # Write the names of three phiosphers
    # to the file
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Buke\n')

    # Close the file.
    outfile.close()
# Call the main function.
main()