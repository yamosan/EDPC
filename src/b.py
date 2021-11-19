N, K = map(int, input().split())
h = [int(i) for i in input().split()]
INF = float("inf")

dp = [INF] * N
dp[0] = 0

for i in range(1, N):
    j_max = K + 1 if i - K >= 0 else i + 1
    for j in range(1, j_max):
        dp[i] = min(dp[i], dp[i - j] + abs(h[i] - h[i - j]))

print(dp[-1])
