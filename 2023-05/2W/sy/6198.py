import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    buildings = []
    for _ in range(N):
        buildings.append(int(sys.stdin.readline()))
    stack = []


    answer = 0
    for i in buildings:
        while len(stack) > 0 and stack[-1] <= i:
            stack.pop()
        stack.append(i)
        answer +=len(stack)-1

    print(answer)
