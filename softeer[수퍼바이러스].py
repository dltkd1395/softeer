import sys

K, P, N = map(int,input().split())

def power(C, n):
	if n == 1:
		return C
	else:
		x = power(C, n//2)
		if n % 2 == 0:
			return x * x %1000000007
		else:
			return x * x * C %1000000007

print(K*power(P, 10*N)%1000000007)
