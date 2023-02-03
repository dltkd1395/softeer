import sys
from itertools import permutations

n,m,k=map(int,input().split())
weight = list(map(int,input().split()))

p = list(permutations(weight, n))

result = float('inf')

for i in p:
    rail = list(i)*m
    sum_weight = 0
    count = 0
    total_weight = 0
    for r in rail:
        if sum_weight + r > m:
            count += 1
            sum_weight = 0
        if count == k:
            result = min(result, total_weight)
            break
            
        sum_weight += r
        total_weight += r
    
print(result)
