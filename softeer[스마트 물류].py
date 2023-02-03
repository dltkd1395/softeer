import sys

n,k=map(int,input().split())

line = list(input())

for i in range(n):
    if line[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0<=j<n:
                if line[j] == 'H':
                    line[j] = 'X'
                    break


print(line.count('X'))
