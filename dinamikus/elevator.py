n, x = map(int, input().split())
w = list(map(int, input().split()))

dp = [(n + 1, 0)] * (1 << n)
dp[0] = (1, 0)

for mask in range(1 << n):
    for i in range(n):
        if mask & (1 << i):
            prev = mask ^ (1 << i)
            rides, weight = dp[prev]

            if weight + w[i] <= x:
                new = (rides, weight + w[i])
            else:
                new = (rides + 1, w[i])

            dp[mask] = min(dp[mask], new)

print(dp[(1 << n) - 1][0])
