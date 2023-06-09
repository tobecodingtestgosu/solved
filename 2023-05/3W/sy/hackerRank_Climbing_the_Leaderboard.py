#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    cache = 0
    answer = []
    ranked = list(dict.fromkeys(ranked))
    ranked.reverse()
    ranked_length = len(ranked)

    for i in range(player_count):
        isPushed = False
        for j in range(cache, ranked_length):
            if player[i] < ranked[j]:
                isPushed = True
                answer.append(ranked_length - j + 1)
                cache = j
                break
            if player[i] == ranked[j]:
                isPushed = True
                answer.append(ranked_length - j)
                cache = j
                break
        if not isPushed:
            answer.append(1)
    return answer

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
