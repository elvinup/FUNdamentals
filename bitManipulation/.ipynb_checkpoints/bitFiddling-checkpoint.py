# Erase lowest set bit
print("Erase lowest set bit of x by doing x & (x-1)")
print("Ex: 44 & 43")
erasedLowestBit = bin(44 & 43)
print(str(bin(44)) + ' & ' + str(bin(43)) + ' = ' + str(bin(44&43)))

# Isolate lowest set bit
print("\nIsolate lowest set bit of x by doing x &~ (x-1)")
print("Ex: 44 &~ 43")
print(str(bin(44)) + ' & ' + str(bin(43)) + ' = ' + str(bin(44&~43)))
