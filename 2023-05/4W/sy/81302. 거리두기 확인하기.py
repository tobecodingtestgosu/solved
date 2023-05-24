from queue import deque


def bfs(x, y, room):
    queue = deque()
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    visited = [[0 for _ in range(5)] for _ in range(5)]
    queue.append((x, y, 0))
    visited[y][x] = 1
    while queue:
        x, y, depth = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                continue
            if room[ny][nx] == "X":
                continue

            if visited[ny][nx] == 0:
                if room[ny][nx] == "P" and depth < 2:
                    return 0
                visited[ny][nx] = 1
                if depth > 2:
                    continue
                queue.append((nx, ny, depth + 1))
    return 1


def solution(places):
    answer = []
    for place in places:
        x = [list(e) for e in place]
        flag = False

        for i in range(5):
            for j in range(5):
                if x[i][j] == "P":

                    print(bfs(j, i, x))
                    if bfs(j, i, x) == 0:
                        flag = True
                        answer.append(0)
                        break
            if flag:
                break
        if not flag:
            answer.append(1)

    return answer