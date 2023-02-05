import sys

n,m = map(int,input().split())

weight = list(map(int,input().split()))

g = [list(map(int,input().split())) for _ in range(m)]

cnt = [1]*(n+1)
cnt[0] = 0

for i in range(m):
    if weight[g[i][0]-1] > weight[g[i][1]-1]:
        cnt[g[i][1]] = 0
    elif weight[g[i][0]-1] < weight[g[i][1]-1]:
        cnt[g[i][0]] = 0
    else:
        cnt[g[i][0]], cnt[g[i][1]] = 0, 0
print(sum(cnt))
