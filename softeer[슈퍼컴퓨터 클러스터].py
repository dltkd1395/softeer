import sys, math


def caluate(minValue):
    cost = 0
    for i in P:
        if i < minValue:
            cost += (minValue-i)**2

            if cost > B:
                return False
    return True

def bSearch():
    start = P[0]
    end = P[-1] + int(math.sqrt(B))
    while start<=end:
        total = 0
        mid = (start+end) // 2
        
        if caluate(mid):
            start = mid + 1
        else:
            end = mid - 1
        
    return start - 1

N, B = map(int,input().split())
P = list(map(int,input().split()))
P = sorted(P)

dic = {}

for i in range(N):
    if P[i] in dic:
        dic[P[i]] += 1
    else:
        dic[P[i]] = 1

print(bSearch()) 
