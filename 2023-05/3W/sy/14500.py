import sys



def bruteforce(x, y,depth,acc):
    global answer
    if depth == 4:
        answer = max(answer,acc)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >=M or ny < 0 or ny >= N:
            continue
        if visited[ny][nx] == 0:
            visited[ny][nx] = 1
            bruteforce(nx, ny, depth+1,acc+paper[ny][nx])
            visited[ny][nx] = 0

def bruteforce2(x, y,depth,acc,flag,before_x=False,before_y=False):
    global answer

    if depth ==3 and not flag:
        bruteforce2(before_x,before_y,depth,acc,True)


    if depth == 4:

        answer = max(answer, acc)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >=M or ny < 0 or ny >= N:
            continue
        if visited[ny][nx] == 0:
            visited[ny][nx] = 1

            bruteforce2(nx, ny, depth+1,acc+paper[ny][nx],False,x,y)

            visited[ny][nx] = 0


if __name__ =="__main__":
    N, M = map(int,sys.stdin.readline().split())
    paper = []
    for i in range(N):
        paper.append(list(map(int,sys.stdin.readline().split())))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    answer =0
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for y in range(N):
        for x in range(M):
            visited[y][x]=1
            bruteforce(x,y,1,paper[y][x])
            visited[y][x] = 0
    for y in range(N):
        for x in range(M):
            visited[y][x] = 1
            bruteforce2(x, y, 1, paper[y][x], False)
            visited[y][x] = 0


    print(answer)




