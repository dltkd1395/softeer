import sys

def test(testSets):
    S = [0]*N
    S[0] = C[0]
    for i in range(N-1):
        if S[i] >= testSets:
            S[i+1] = C[i+1] + D[i]
        elif S[i] + D[i] >= testSets:
            S[i+1] = C[i+1] + (S[i]+D[i]-testSets)
        else:
            return False


    if S[N-1] >= testSets:
        return True
    else:
        return False

def binary_search(start, end):
    
    while start<end:
        mid = (start+end+1)//2

        if test(mid):
            start = mid
        else:
            end = mid - 1
    return start

N, T = map(int,input().split())

for _ in range(T):
    C = [0]*N
    D = [0]*N
    Temp = list(map(int,input().split()))
    for i in range(N-1):
        C[i] = Temp[i*2]
        D[i] = Temp[i*2+1]
    C[N-1] = Temp[2*(N-1)]
    print(binary_search(0, 2*10**12))
