# Problem 3: Longest Non-Decreasing Subsequence with XOR constraint
import sys
from collections import defaultdict

data = sys.stdin.read().strip().split()
if not data:
    print(0)
    sys.exit(0)
it = iter(data)
N = int(next(it))
M = int(next(it))
A = [0]*N
for i in range(N):
    A[i] = int(next(it))

dp = [dict() for _ in range(N)]  # dp[i]: xor -> length
res = 0
for i in range(N):
    # single element subsequence
    dp[i][A[i]] = 1
    if A[i] >= M:
        res = max(res, 1)
    for j in range(i):
        if A[j] <= A[i]:
            # extend subsequences ending at j
            dj = dp[j]
            # iterate items
            for xr, l in dj.items():
                nx = xr ^ A[i]
                nl = l + 1
                if dp[i].get(nx, 0) < nl:
                    dp[i][nx] = nl
                    if nx >= M and nl > res:
                        res = nl
print(res)
