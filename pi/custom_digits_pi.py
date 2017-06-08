#!/usr/bin/python3


'''

Print out pi up to N number of digits

We implemented the Bailey-Borwein-Plouffe formula to calculate
a custom precision of pi.

Usage:

./custom_digits_pi.py 15
3.14159265358979

'''

from sys import argv
from math import factorial
from decimal import Decimal, getcontext


def custom_digits_pi(n=10):
    getcontext().prec=n
    print(sum(1 / Decimal(16)**k *
              (Decimal(4) / (8 * k + 1) -
               Decimal(2) / (8 * k + 4) -
               Decimal(1) / (8 * k + 5) -
               Decimal(1) / (8 * k + 6)) for k in range(n)))

if __name__ == "__main__":
    custom_digits_pi(int(argv[1]))
