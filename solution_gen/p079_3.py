

# Solution

#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(Q):
    # Write your code here
    Q = sorted(Q)
    min_b = (
        Q[2] - Q[1] - 2
    )
    if (len(Q) == 3):
        exit(1)
    elif (len(Q) == 4):
        if (Q[1] - (3-len(Q)) < min_b):
            min_b = Q[1] - (3-len(Q))

    elif (len(Q) < 3):
        exit(1)
    else:
        for i

# Q = input().rstrip().split()
# minimumBribes(Q)
