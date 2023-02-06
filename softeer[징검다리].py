import sys

N = int(input())
rocks = list(map(int,input().split()))

dp = [1]*N
answer = 0
for i in range(1, N):
    for j in range(i):
        if 1 <= rocks[j] < rocks[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
    
