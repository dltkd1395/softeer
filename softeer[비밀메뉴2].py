import sys
from itertools import combinations

N,M,K = map(int,input().split())

A = list(input().split())
B = list(input().split())
dp = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + 1
answer = 0
for i in dp:
    answer = max(answer, max(i))

print(answer)
