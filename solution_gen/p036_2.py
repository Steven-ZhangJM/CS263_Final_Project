

a = 1

# Base 2

while a <= 1000000:
	if str(bin(a)) == str(bin(a))[::-1] and str(oct(a)) == str(oct(a))[::-1] and str(hex(a)) == str(hex(a))[::-1]:
		print(a, " : ", bin(a), oct(a), hex(a))
	a = a + 1

a = 1

# Base 10

while a <= 1000000:
	if str(a) == str(a)[::-1] and str(bin(a)) == str(bin(a))[::-1] and str(oct(a)) == str(oct(a))[::-1] and str(hex(a)) == str(hex(a))[::-1]:
		print(a, " : ", bin(a), oct(a), hex(a))
	a = a + 1
