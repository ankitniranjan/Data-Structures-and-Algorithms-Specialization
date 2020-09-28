#!/usr/bin/env python3
import time

def MaxPairwiseProductFast(numbers):
    first_max = max(numbers)
    numbers.remove(first_max)
    sec_max = max(numbers)
    return first_max * sec_max

if __name__ == '__main__':
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(MaxPairwiseProductFast(numbers))
