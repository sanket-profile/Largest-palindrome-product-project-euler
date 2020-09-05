lowlimit = 100
uplimit = 999
maxpal = 0
for i in range(uplimit , lowlimit-1 , -1):
	for j in range(i , lowlimit-1 , -1):
		mul = str(i *j)
		if len(mul) == 6:
			if mul[:3][::-1] == mul[3:]:
				a = int(mul)
				if a > maxpal:
					maxpal = a
					m = i
					n = j
					lowlimit = j
				else:
					pass
			else:
				pass
		else:
			if mul[:2][::-1] == mul[3:]:
				a = int(mul)
				if a > maxpal:
					maxpal = a
					lowlimit = j
				else:
					pass
			else:
				pass
print(maxpal , m , n)
