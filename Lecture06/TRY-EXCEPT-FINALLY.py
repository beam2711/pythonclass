# Code to show how try-exceot-else-finally use
def main():
    a, b = map(int, input("Input 2 integer values: ").split())
    divide(a, b)

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("excuting finally clause")

main()