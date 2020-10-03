#!/usr/bin/env python3
import time

def MaxPairwiseProductFast(numbers):
    first_max = max(numbers)    #Fetching Largest Number
    numbers.remove(first_max)   #Removing first_max from list
    sec_max = max(numbers)      #Fetching Second Largest Number from the modified list
    return first_max * sec_max      

if __name__ == '__main__':
    n = int(input())
    numbers = [int(x) for x in input().split()]
    print(MaxPairwiseProductFast(numbers))
