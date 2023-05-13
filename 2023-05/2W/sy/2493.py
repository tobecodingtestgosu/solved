import sys

if __name__ =="__main__":
    N = int(sys.stdin.readline())
    towers = list(map(int,sys.stdin.readline().split()))
    stack = []
    answer = [0 for _ in range(len(towers))]

    stack.append((0,towers[0]))
    for i in range(1,len(towers)):
        while len(stack) > 0 and stack[-1][1] <= towers[i]:
            stack.pop()
        if  len(stack) > 0 and stack[-1][1] > towers[i]:
            answer[i]=stack[-1][0]+1
        stack.append((i,towers[i]))
    print(*answer)
