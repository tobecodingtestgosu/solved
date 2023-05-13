import sys



if __name__ =="__main__":
    n, k = map(int, sys.stdin.readline().split())

    coins = []
    dp = [100001 for _ in range(k+1)]
    for _ in range(n):
        coins.append(int(sys.stdin.readline()))
    dp[0]=0

    for coin in coins:
        for i in range(coin,k+1):
            if i >=coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)




    if dp[k] !=100001:
        print(dp[k])
    else:
        print(-1)






