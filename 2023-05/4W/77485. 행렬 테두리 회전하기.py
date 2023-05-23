def swap(x, y, value):
    global cache
    temp = matrix[x][y]
    matrix[x][y] = cache
    cache = temp


def solution(rows, columns, queries):
    answer = []
    matrix = []
    count = 1
    for i in range(rows):
        arr = []
        for j in range(columns):
            arr.append(count)
            count += 1
        matrix.append(arr)

    for query in queries:
        min_num = 10 ** 9
        x = query[0] - 1
        y = query[1] - 1
        cache = matrix[x + 1][y]
        while y <= query[3] - 1:
            min_num = min(min_num, matrix[x][y])
            temp = matrix[x][y]
            matrix[x][y] = cache

            cache = temp
            y += 1
        y -= 1
        x += 1
        while x <= query[2] - 1:
            min_num = min(min_num, matrix[x][y])
            temp = matrix[x][y]
            matrix[x][y] = cache
            cache = temp
            x += 1
        y -= 1
        x -= 1
        while y >= query[1] - 1:
            min_num = min(min_num, matrix[x][y])
            temp = matrix[x][y]
            matrix[x][y] = cache
            cache = temp
            y -= 1
        x -= 1
        y += 1
        while x >= query[0] - 1:
            min_num = min(min_num, matrix[x][y])
            temp = matrix[x][y]
            matrix[x][y] = cache
            cache = temp
            x -= 1
        answer.append(min_num)