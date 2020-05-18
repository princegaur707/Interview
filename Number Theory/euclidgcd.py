from math import gcd
def eugcd(a,b):
	if a == 0:
		return b
	return eugcd(b%a,a)

t = int(input())
while t:
	a,b = map(int,input().split())
	print(gcd(a,b))
	print(eugcd(a,b))
	t=t-1
