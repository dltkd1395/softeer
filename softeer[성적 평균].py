import sys

input = sys.stdin.readline

n,k=map(int,input().split())

score = list(map(int,input().split()))

for _ in range(k):
    start, end = map(int,input().split())

    result = round(sum(score[start-1: end])/(end-start+1),2)
    print("{:.2f}".format(result))
