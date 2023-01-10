#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    arg = len(sys.argv) - 1
    if arg != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if ops == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, add(a, b)))
    elif ops == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, sub(a, b)))
    elif ops == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, div(a, b)))
    elif ops == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
