import sys

N = int(input())
line = []
for i in range(N-1):
    line.append(list(map(int,input().split())))

A, B = map(int,input().split())

time_a, time_b, work_a, work_b = 0,0,0,0

for i in range(N-1):
    time_a = min(line[i][0] + work_a, line[i][1] + line[i][3] + work_b)
    time_b = min(line[i][1] + work_b, line[i][0] + line[i][2] + work_a)

    work_a, work_b = time_a, time_b

print(min(time_a+A,time_b+B))
