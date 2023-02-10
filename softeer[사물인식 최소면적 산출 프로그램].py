import sys

N, K = map(int, input().split())
color = [[] for i in range(K + 1)]
result = [10**9]
for _ in range(N):
    x,y,z = map(int, input().split())
    color[z].append((x, y))

def dfs(sx,sy,ex,ey, depth, current):

    if depth == K + 1:
        if result[0] > current:
            result[0] = current
        return

    for p in color[depth]:
        x1, x2, y1, y2 = sx, ex, sy, ey
        if p[0] < sx:
            x1 = p[0]
        elif p[0] > ex:
            x2 = p[0]
        if p[1] < sy:
            y1 = p[1]
        elif p[1] > ey:
            y2 = p[1]
        
        tmp = abs(x1-x2)*abs(y1-y2)

        if tmp < result[0]:
            dfs(x1,y1,x2,y2,depth+1, tmp)

for x,y in color[1]:
    dfs(x,y,x,y, 2, 0)

print(result[0])
