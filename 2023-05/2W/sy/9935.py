if __name__ =="__main__":
    explosiveString = list(sys.stdin.readline().rstrip())
    bombString = list(sys.stdin.readline().rstrip())
    stack = []
    for i in explosiveString:
        stack.append(i)
        if len(stack) >= len(bombString):
            if stack[len(stack)- len(bombString) :len(stack)] == bombString:
                for _ in range(len(bombString)):
                    stack.pop()
    if len(stack) ==0:
        print('FRULA')
    else:
        print(''.join(stack))