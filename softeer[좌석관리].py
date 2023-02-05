import sys,math


n,m,q = map(int,input().split())

ID = [0]*(10**4+1)
seat = [[0]*(m+2) for _ in range(n+2)]

def nearest(x,y):
    min_d = 1000
    for i in range(1,n+1):
        for j in range(1,m+1):
            if seat[i][j]:
                d = (x-i)**2 + (y-j)**2
                if d < min_d:
                    min_d = d
    return min_d

def assign(pid):
    max_d = 0

    for i in range(1,n+1):
        for j in range(1,m+1):
            if seat[i][j] == 0 and seat[i-1][j] == 0 \
            and seat[i][j-1] == 0 and seat[i+1][j] == 0 and seat[i][j+1] == 0:
                d = nearest(i,j)
                if max_d < d:
                    max_d = d
                    ID[pid] = [i,j]
    if max_d == 0:
        return False
    else:
        seat[ID[pid][0]][ID[pid][1]] = 1
        return True
for i in range(q):
    inOut, pid = input().split()
    pid = int(pid)

    if inOut == 'In':
        if ID[pid] == 0:
            if assign(pid):
                print(f'{pid} gets the seat ({ID[pid][0]}, {ID[pid][1]}).')
            else:
                print('There are no more seats.')
        elif ID[pid] == 1:
            print(f'{pid} already ate lunch.')
        else:
            print(f'{pid} already seated.')
    else:
        if ID[pid] == 0:
            print(f'{pid} didn\'t eat lunch.')
        elif ID[pid] == 1:
            print(f'{pid} already left seat.')
        else:
            print(f'{pid} leaves from the seat ({ID[pid][0]}, {ID[pid][1]}).')
            seat[ID[pid][0]][ID[pid][1]] = 0
            ID[pid] = 1

