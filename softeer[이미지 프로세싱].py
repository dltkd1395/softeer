import sys
from collections import deque

dx = [1,0,0,-1]
dy = [0,1,-1,0]

def bfs(i,j,c):
    visited = [[0]*W for _ in range(H)]
    visited[i][j] = 1
    q = deque([[i,j]])
    F = maps[i][j]
    maps[i][j] = c
    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = dx[d]+x
            ny = dy[d]+y

            if 0<=nx<H and 0<=ny<W:
                if visited[nx][ny] == 0 and  maps[nx][ny] == F:
                    visited[nx][ny] = 1
                    maps[nx][ny] = c
                    q.append([nx,ny])

H, W = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(H)]

Q = int(input())

for _ in range(Q):
    i,j,c = map(int,input().split())
    bfs(i-1,j-1,c)

for i in maps:
    print(*i)
