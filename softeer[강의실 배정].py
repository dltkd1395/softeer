import sys
import heapq

n = int(sys.stdin.readline())

pq = []

for _ in range(n):
    s, f = list(map(int,sys.stdin.readline().split()))
    heapq.heappush(pq, (f, s))

answer = 0
finish_time = 0
while pq:
    if pq[0][1] >= finish_time:
        finish_time= heapq.heappop(pq)[0]
        answer += 1
        continue

    heapq.heappop(pq)
print(answer)
