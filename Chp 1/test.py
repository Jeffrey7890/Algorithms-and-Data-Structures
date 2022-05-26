day = 3
month = 7
n = 0
cnt = 0
thirty = [8,4,6,11]
print("Su\tMo\tTu\tWe\tTh\tFr\tSa")
for i in range(5):
	for j in range(7):
		if cnt < day:
			print(" ", end="\t")
		else:
			n+=1
			print(n, end = "\t")
		cnt+=1
		if month in thirty and n == 30:
			break 
		elif n == 31:
			break

	print(" ")