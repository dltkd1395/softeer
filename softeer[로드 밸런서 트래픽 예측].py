import sys
from collections import deque

N, K = map(int,input().split())

indegree = [0] * (N + 1)
graph = [[] for i in range(N + 1)]

for i in range(1, N+1):
    S = list(map(int, input().split()))
    graph[i] = S[1:]
    for j in range(1, S[0]+1):
        indegree[S[j]] += 1

def topology_sort():
    odering = []
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        odering.append(now)
        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    return odering


odering = topology_sort()

traffic = [0]*(N+1)
traffic[1] = K
for i in range(N):
    node = odering[i]
    request = traffic[node]

    if not graph[node]:
        continue

    l = len(graph[node])
    quotient = request//l
    remander = request%l

    for j in range(l):
        child = graph[node][j]
        traffic[child] += quotient
    
    for j in range(remander):
        child = graph[node][j]
        traffic[child] += 1

print(*traffic[1:])
