def isleapyear(l):
	flag1 = l%4 == 0 and l%100 != 0
	flag2 = l%400 == 0
	if flag1 or flag2:
		return True
	else:
		return False

t = int(input())
while t:
	leapyear = int(input())
	print(isleapyear(leapyear))
	t=t-1
