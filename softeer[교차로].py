import sys
from collections import deque

N = int(input())
    
queues = [deque() for _ in range(4)]
for i in range(N):
    t, w = input().split()
    t = int(t)
    queues[ord(w)-ord('A')].append((i, t))

answer = [-1]*N
is_waiting = [0]*4
current = -1
while queues[0] or queues[1] or queues[2] or queues[3]:
    min_time = int(1e9)

    for i in range(4):
        if queues[i]:
            time = queues[i][0][1]
            min_time = min(min_time, time)

            if time <= current:
                is_waiting[i] = 1
    total_waiting = sum(is_waiting)
    if total_waiting == 4:
        break
    
    if total_waiting == 0:
        current = min_time
        continue
    
    for i in range(4):
        if is_waiting[i] and not is_waiting[(i-1)%4]:
            idx, _ = queues[i].popleft()
            answer[idx] = current
    
    is_waiting = [0]*4
    current += 1

print(*answer, sep='\n')

