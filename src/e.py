N, W = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(N)]

MAX_V = (10 ** 3) * (10 ** 2)
INF = float("inf")
dp = [[INF] * (MAX_V + 1) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0] = 0

for i in range(1, N + 1):
    for v in range(1, MAX_V + 1):
        if v - wv[i - 1][1] < 0:
            dp[i][v] = dp[i - 1][v]
        else:
            dp[i][v] = min(dp[i - 1][v], dp[i - 1][v - wv[i - 1][1]] + wv[i - 1][0])

ans = 0
for v in range(1, MAX_V + 1):
    if dp[N][v] <= W:
        ans = max(ans, v)
print(ans)
