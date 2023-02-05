import sys
from collections import deque

dx = [1,0,0,-1]
dy = [0,1,-1,0]

def bfs():
    visited = [[-1]*M for _ in range(N)]
    visited[0][0] = 0
    q = deque([[0,0]])

    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y

            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny] == -1:
                    if maps[nx][ny] >= 1:
                        maps[nx][ny] += 1
                    else:
                        visited[nx][ny] = 0
                        q.append([nx,ny])

N, M = map(int,input().split())

maps = [list(map(int,input().split())) for _ in range(N)]

answer = 0

while True:
    bfs()
    flag = False
    for i in range(N):
        for j in range(M):
            if maps[i][j] >= 3:
                maps[i][j] = 0
                flag = True
            elif maps[i][j] == 2:
                maps[i][j] = 1         
    if not flag:
        break
    else:
        answer+=1
print(answer)
