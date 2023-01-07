#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    lenQ = len(q)
    sortedQ = [i+1 for i in range(lenQ)]
    count = [0]*lenQ

    while q != sortedQ:
        for i in range(lenQ-1):
            if q[i] > q[i+1]:
                count[q[i]-1] += 1
                if count[q[i]-1] > 2:
                    print('Too chaotic')
                    return
                q[i], q[i+1] = q[i+1], q[i]

    print(sum(count))


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
