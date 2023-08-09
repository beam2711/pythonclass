def main():
    number = int(input('Enter a nonnegative integer: '))
    fact = factorial(number)
    print('The factorial of', number, 'is', fact)
def factorial(num):
    if  num == 0:
        return 1
    else:
        return num * factorial(num - 1)
main()





def main():
    print('I Love Python')
    print()
    print('My Lucky No. is 7')
main()