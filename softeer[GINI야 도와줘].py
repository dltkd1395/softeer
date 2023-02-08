import sys
from collections import deque

dx = [1,0,0,-1]
dy = [0,1,-1,0]

def spread():
    global rain
    tmp = []
    for i in rain:
        x, y = i

        for d in range(4):
            nx = dx[d]+x
            ny = dy[d]+y

            if 0<=nx<R and 0<=ny<C:
                if maps[nx][ny] == '.':
                    maps[nx][ny] = '*'
                    tmp.append((nx,ny))
    tmp = rain+tmp
    rain = list(set(tmp))
    return        

def bfs(i,j):
    visited[i][j] = 1
    q = deque([[i,j,0]])
    spread()
    tmp = 0
    while q:
        x,y,c = q.popleft()
        if tmp != c:
            spread()
        tmp = c

        for d in range(4):
            nx = dx[d]+x
            ny = dy[d]+y
            if 0<=nx<R and 0<=ny<C:
                if maps[nx][ny] == 'H':
                    return c+1

                if visited[nx][ny] == 0 and maps[nx][ny] =='.':
                    visited[nx][ny] = 1
                    q.append([nx,ny,c+1])
    return 'FAIL'

R, C = map(int,input().split())

maps = [['.']*C for _ in range(R)]
visited = [[0]*C for _ in range(R)]
start = [0,0]

rain = []
for i in range(R):
    M = list(input())
    for j in range(C):
        if M[j] == 'W':
            start = [i,j]
        elif M[j] == '*':
            rain.append((i,j))
    maps[i] = M

print(bfs(start[0], start[1]))
