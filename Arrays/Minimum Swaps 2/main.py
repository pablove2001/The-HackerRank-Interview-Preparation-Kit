#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    countS = 0

    arrS = [i+1 for i in range(len(arr))]

    while arr != arrS:
        for i in range(len(arr)):
            if arr[i] != i+1:
                arr[arr[i]-1], arr[i] = arr[i], arr[arr[i]-1]
                countS += 1

    return countS


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
