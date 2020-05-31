#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    j = n-1
    for i in range(1,n+1):
        print(' '*j + '#'*i)
        j -=1

if __name__ == '__main__':
    n = int(input())

    staircase(n)
