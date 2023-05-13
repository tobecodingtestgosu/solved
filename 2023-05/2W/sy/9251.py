import sys

if __name__ =="__main__":
    string1 = sys.stdin.readline().rstrip()
    string2 = sys.stdin.readline().rstrip()
    dp = [[0 for _ in range(len(string1)+1)] for _ in range(len(string2)+1)]

    for i in range(1,len(string2)+1):
        for j in range(1,len(string1)+1):


            if string1[j-1] == string2[i-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])



    print(dp[-1][-1])
