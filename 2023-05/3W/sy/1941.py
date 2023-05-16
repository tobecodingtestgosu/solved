import sys
from itertools import combinations
from collections import deque

def bfs(x,y):
    global answer
    queue =deque()
    queue.append((x,y,girls[y][x]))

    visited[y][x] = 0
    count = 1
    stack = []
    stack.append((x, y, girls[y][x]))

    while queue:
        xx, yy, zz = queue.popleft()
        if count == 7:

            som_count = 0
            for i in range(7):
                if stack[i][2] =='S':
                    som_count +=1
            if som_count >=4:
                try:
                    if answer_arr.index(sorted(stack)):
                        return
                except:
                    answer_arr.append(sorted(stack))
                    return
            else:
                return



        for i in range(4):
            nx = xx+ dx[i]
            ny = yy+ dy[i]
            if nx < 0  or nx > 4 or ny < 0 or ny > 4:
                continue

            if visited[ny][nx] == 1:
                visited[ny][nx]=0
                queue.append((nx,ny,girls[ny][nx]))
                stack.append((nx,ny,girls[ny][nx]))
                count +=1

if __name__ =="__main__":
    answer =0
    answer_arr =[]
    girls = []
    arr =[]
    for i in range(5):
        girls.append(list(sys.stdin.readline().rstrip()))
    for i in range(5):
        for j in range(5):
            arr.append((i,j,girls[j][i]))


    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    comb =list(combinations(arr,7))
    for i in comb:
        visited = [[0 for _ in range(5)] for _ in range(5)]
        for y,x,z in i:
            visited[y][x] =1
        bfs(i[0][1],i[1][0])
    print(len(answer_arr))



