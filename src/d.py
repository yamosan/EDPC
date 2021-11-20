N, W = map(int, input().split())
lis = [[int(i) for i in input().split()] for i in range(N)]
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for w in range(1, W + 1):
        if w - lis[i - 1][0] >= 0:
            dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - lis[i - 1][0]] + lis[i - 1][1])
        else:
            dp[i][w] = dp[i - 1][w]

print(dp[N][W])
