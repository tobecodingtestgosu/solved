#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#


def countRight(x, y, obstaclesDict):
    for i in range(x, n):
        if obstaclesDict.get(i) and y in obstaclesDict[i]:
            return i - x - 1
    return n - x - 1


def countLeft(x, y, obstaclesDict):
    for i in range(x, -1, -1):
        if obstaclesDict.get(i) and y in obstaclesDict[i]:
            return x - i - 1
    return x


def countUp(x, y, obstaclesDict):
    for i in range(y, -1, -1):
        if obstaclesDict.get(x) and i in obstaclesDict[x]:
            return y - i - 1
    return y


def countDown(x, y, obstaclesDict):
    for i in range(y, n):
        if obstaclesDict.get(x) and i in obstaclesDict[x]:
            return i - y - 1
    return n - y - 1


def countUpRight(x, y, obstaclesDict):
    for i in range(1, min(n - x, y)):
        if obstaclesDict.get(x + i) and y - i in obstaclesDict[x + i]:
            return i - 1
    return min(n - x - 1, y)


def countUpLeft(x, y, obstaclesDict):
    for i in range(1, n - min(x, y)):
        if obstaclesDict.get(x - i) and y - i in obstaclesDict[x - i]:
            return i - 1
    return min(x, y)


def countDownLeft(x, y, obstaclesDict):
    for i in range(1, n - min(x, y)):
        if obstaclesDict.get(x - i) and y + i in obstaclesDict[x - i]:
            return i - 1
    return min(x, n - y - 1)


def countDownRight(x, y, obstaclesDict):
    for i in range(1, n - max(n - x, y)):
        if obstaclesDict.get(x + i) and y + i in obstaclesDict[x + i]:
            return i - 1
    return n - max(x, y) - 1


def queensAttack(n, k, r_q, c_q, obstacles):
    q_y = n - c_q
    q_x = r_q - 1
    count = 0

    obstaclesDict = {}
    for x, y in obstacles:
        if obstaclesDict.get(x - 1):
            obstaclesDict[x - 1].append(n - y)
        else:
            obstaclesDict[x - 1] = [n - y]
    for i in obstaclesDict.keys():
        obstaclesDict[i].sort()

    count += countLeft(q_x, q_y, obstaclesDict)
    count += countRight(q_x, q_y, obstaclesDict)
    count += countUp(q_x, q_y, obstaclesDict)
    count += countDown(q_x, q_y, obstaclesDict)
    count += countUpRight(q_x, q_y, obstaclesDict)
    count += countUpLeft(q_x, q_y, obstaclesDict)
    count += countDownLeft(q_x, q_y, obstaclesDict)
    count += countDownRight(q_x, q_y, obstaclesDict)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
