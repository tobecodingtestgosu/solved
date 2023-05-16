import sys
from collections import deque







if __name__ == "__main__":
    M, N, H = map(int, sys.stdin.readline().split())
    tomatoes = [[] for _ in range(H)]
    queue = deque()
    for i in range(H-1,-1,-1):
        for _ in range(N):
            tomatoes[i].append(list(map(int,sys.stdin.readline().split())))

    day = 0

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomatoes[z][y][x] ==1:
                    queue.append((x,y,z,day))



    dx =[1,0,-1,0]
    dy = [0,-1,0,1]
    dz = [-1, 1]


    while queue:
        x, y, z,count= queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < M and 0 <= ny < N:

                if tomatoes[z][ny][nx] ==0:
                    queue.append((nx, ny, z,count+1))
                    tomatoes[z][ny][nx] = 1
        for i in range(2):
            nz = dz[i] + z
            if 0 <= nz < H:
                if tomatoes[nz][y][x] == 0:
                    queue.append((x, y, nz,count+1))
                    tomatoes[nz][y][x] = 1
        day =count

    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomatoes[z][y][x] == 0:
                    day =-1
                    break
    print(day)










