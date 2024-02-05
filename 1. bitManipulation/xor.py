# The XOR of a group of bits is its parity
# Parity is 1 if theres an odd amount of bits in a binary word (0111), 0 if even (0110)
x = int('11010111', 2)
x ^= x >> 4
print("x ^= x >> 4 -> %s" % str(bin(x)))
print('The parity of 11010111 is the same as the parity of 1101 XOR(^) 0111, aka 1010')
x ^= x >> 2
print("x ^= x >> 2 -> %s" % str(bin(x)))
print('The parity of 1010 is the same as the parity of 10 ^ 10, aka 00')
x ^= x >> 1
print("Just bitwise & the last bit by 1 for the final parity")
print("x ^= x >> 1 -> %s" % str(bin(x)))
print(x & 0x1)
#print(bin(x ^ (x >> 4)))
#print(bin(x ^ (x >> 32)))