#Left shifting essentially doubles a number

numToDouble = 2

print('Shifting iteratively on 2')
for i in range(3):
	
	print(str(numToDouble) + ' << ' + str(i) + ' = ' + str(numToDouble << i))
		

for i in range(3):
	numToDouble <<= i
	
	print("Cumulative: " + str(numToDouble))
