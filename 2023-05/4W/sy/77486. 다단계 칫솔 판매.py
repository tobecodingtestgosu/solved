def solution(enroll, referral, seller, amount):
    answer = [0 for _ in range(len(enroll))]
    graph = {}
    for i in range(len(enroll)):
        graph[enroll[i]] = (i, referral[i])

    def calculate(referral_person, profit):
        nonlocal enroll

        idx = referral_person[0]

        fee = profit // 10
        if fee < 1:
            answer[idx] += profit
            return
        else:
            answer[idx] += profit - fee
            if referral[idx] != '-':
                calculate(graph[referral_person[1]], fee)

    for i in range(len(seller)):
        calculate(graph[seller[i]], amount[i] * 100)


    return answer