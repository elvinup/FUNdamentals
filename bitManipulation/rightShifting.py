#Right shifting essentially halves a number

numToDouble = 8

print('Shifting iteratively on 8')
for i in range(3):
	
	print('i >> ' + str(i) + ' = ' + str(numToDouble >> i))
		

for i in range(3):
	numToDouble >>= 1
	
	print("Cumulative: " + str(numToDouble))
