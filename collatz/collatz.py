#!/usr/bin/python3

def collatz(n):
    count = 0

    while n != 1:
        if (n % 2 == 0):
            n = n / 2
        else:
            n = 3 * n + 1
        count += 1

    return count


print(collatz(27))  # should be 111