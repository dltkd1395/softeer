import sys
from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]

direction = ['>','v','<','^']

def check(x, y):
    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '#':
            start = direction[i]
            cnt += 1

    if cnt > 1:
        return False

    return start

def bfs(board, visited, i,j):

    visited[i][j] = 1
    q = deque([[i,j]])
    path = deque()
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y

            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] == 0 and board[nx][ny] == '#':
                    visited[nx][ny] = 1
                    path.append(d)
                    q.append([nx,ny])
    return path

n,m = map(int,input().split())

board = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
path = ''

for i in range(n):
    for j in range(m):
        if board[i][j] == '#' and check(i,j):
            dir = bfs(board,visited,i,j)
            print(i+1, j+1)
            print(direction[dir[0]])

            cnt = 1
            before = dir.popleft()
            for d in dir:
                if before == d:
                    cnt += 1
                    before = d

                    if cnt%2==0:
                        path += 'A'
                        cnt = 0
                else:
                    if (before-1)%4 == d:
                        path += 'L'
                    else:
                        path += 'R'
                    before = d
                    cnt = 1 
            print(path)
            sys.exit() 
