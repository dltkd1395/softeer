import sys

N = int(input())

bus = list(map(int,input().split()))

answer = 0
for i in range(N):
    circle = 0
    for j in range(i+1,N):
        if bus[i] < bus[j]:
            circle += 1
        elif bus[i] > bus[j]:
            answer += circle

print(answer)
