import sys
from collections import Counter
if __name__ =="__main__":
    N = int(sys.stdin.readline())
    A = list(map(int,sys.stdin.readline().split()))
    stack = []
    answer = [-1 for _ in range(N)]
    countArr = Counter(A)
    stack.append(0)
    for i in range(1,N):
        while len(stack) >0 and countArr[A[stack[-1]]] < countArr[A[i]]:
            answer[stack.pop()] = A[i]
        stack.append(i)
    print(*answer)
