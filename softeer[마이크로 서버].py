import sys
from collections import Counter

T = int(input())

for _ in range(T):
    N = int(input())
    task = list(map(int,input().split()))
    task.sort()

    num300 = task.count(300)
    start = num300
    end = N-1
    servers = 0
    while start<=end:
        servers += 1

        if task[end] > 600:
            end-=1
            continue
        elif start != end and task[start] + task[end] <= 900:
            start += 1
        elif num300 > 0:
            num300 -= 1
        end -= 1
    servers += (num300+2)//3
    print(servers)
