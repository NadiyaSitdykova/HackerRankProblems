def get(dp, i, j):
    if i < 0:
        return 0
    return dp[i][j]

def make_change(coins, n):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(n+1):
        for j in range(1, m+1):
            k = coins[j-1]
            dp[i][j] = get(dp, i-k, j) + dp[i][j-1]
    return dp[n][m]
    

n,m = map(int, raw_input().strip().split(' '))
coins = map(int,raw_input().strip().split(' '))
print make_change(coins, n)
