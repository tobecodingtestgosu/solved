import sys

if __name__ =="__main__":
    N = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))
    stack = []
    answer = [-1 for _ in range(len(A))]
    stack.append(0)
    for i in range(1,len(A)):
        if len(stack) > 0 and A[stack[-1]] < A[i]:
            while len(stack) > 0 and A[stack[-1]] < A[i]:

                answer[stack.pop()] = A[i]

        stack.append(i)
    print(*answer)
