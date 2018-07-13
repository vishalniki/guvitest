n=input()
factorial=1
if n<0:
	print("the factoiral is not valied")
elif n==0:
	print("the factorial 0 is 1")
else:
	for i in range (1,n+1):
		factorial=factorial*i
print(factorial)
