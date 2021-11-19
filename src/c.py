N = int(input())
lis = [[int(i) for i in input().split()] for _ in range(N)]

dp = [[-1] * 3 for _ in range(N)]
dp[0] = lis[0]

for i in range(1, N):
    dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + lis[i][0]
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + lis[i][1]
    dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + lis[i][2]

print(max(dp[N - 1]))
