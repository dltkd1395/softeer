import sys
from collections import defaultdict, deque

N, T =map(int,input().split())

signs = defaultdict(list)

inter = {1: ['up', 'down', 'right'] , 2: ['left', 'up', 'right'], 3: ['left', 'up', 'down'],\
           4: ['left', 'down', 'right'], 5: ['up', 'right'], 6: ['left', 'up'], 7: ['left', 'down'],\
           8: ['down', 'right'], 9: ['down', 'right'], 10: ['up', 'right'], 11: ['left', 'up'],\
           12: ['left', 'down']}
           
directions =  {'left' : [0, -1], 'right' : [0, 1], 'up' : [-1, 0], 'down' : [1, 0]} 

prev_direction = {'up' : [2, 6, 10], 'right' : [1, 5, 9], 'down' : [4, 8, 12], 'left' : [3, 7, 11]} # 북 동 남 서

for i in range(N):
    for j in range(N):
        signs[(i,j)].extend(list(map(int,input().split())))

q = deque([[0, 0, 0, 'up']])
check = set()
result = set()
while q:
    x,y , time, direction = q.popleft()
    check.add((x, y, time%4, direction))
    result.add((x, y))
    ops = inter[signs[(x,y)][time%4]]
    if signs[(x,y)][time%4] not in prev_direction[direction]:
        continue
    for op in ops:
        dx, dy = directions[op]
        nx ,ny = x+dx, y+dy
        if 0<=nx<N and 0<=ny<N and (time+1) <= T and ((nx, ny, (time+1)%4, op) not in check):
            q.append([nx, ny, time+1, op])
print(len(set(result)))
