from collections import deque


def solution(queue1, queue2):
    deque1 = deque(queue1)
    deque2 = deque(queue2)
    countLimit = max(len(deque1), len(deque2))
    count = 0

    sum1 = sum(deque1)
    sum2 = sum(deque2)
    while True:
        if sum1 > sum2:
            ele = deque1.popleft()
            deque2.append(ele)
            count += 1
            sum2 += ele
            sum1 -= ele
        elif sum1 < sum2:
            ele = deque2.popleft()
            deque1.append(ele)
            count += 1
            sum1 += ele
            sum2 -= ele
        else:
            return count
        if countLimit * 3 < count:
            break

    return -1