#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10000)


#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#


def swapNodes(indexes, queries):
    answer = []

    def inOrderTraversal(index, depth, query):
        if depth % query == 0:
            temp = indexes[index - 1][0]
            indexes[index - 1][0] = indexes[index - 1][1]
            indexes[index - 1][1] = temp

        if indexes[index - 1][0] != -1:
            inOrderTraversal(indexes[index - 1][0], depth + 1, query)

        before.append(index)

        if indexes[index - 1][1] != -1:
            inOrderTraversal(indexes[index - 1][1], depth + 1, query)

    for query in queries:
        before = []
        inOrderTraversal(1, 1, query)
        answer.append(before)
    return answer

    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
