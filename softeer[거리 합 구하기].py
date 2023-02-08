import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

N = int(input())
nodes = [[] for i in range(N+1)]
for _ in range(N-1):
    x, y, t = map(int, input().split())
    nodes[x].append((y, t))
    nodes[y].append((x, t))

subSize = [0 for i in range(N+1)]
dist = [0 for i in range(N+1)]
def dfs(cur, par) :
    subSize[cur] = 1
    for idx in range(len(nodes[cur])) : 
        child, weight = nodes[cur][idx]
        
        if child != par : 
            dfs(child, cur)
            dist[cur] += subSize[child] * weight + dist[child]
            subSize[cur] += subSize[child]
            
def dfs2(cur, par) : 
    for idx in range(len(nodes[cur])): 
        child, weight = nodes[cur][idx]
        if child != par : 
            dist[child] = dist[cur] + weight * (N-subSize[child]-subSize[child])
            dfs2(child, cur)

dfs(1,1)
dfs2(1,1)

for idx in range(1, N+1) : 
    print(dist[idx])
