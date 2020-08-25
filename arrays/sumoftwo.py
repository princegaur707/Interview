def Add(x, y): 

	while (y != 0): 
	
		# carry now contains common 
		# set bits of x and y 
		carry = x & y 

		# Sum of bits of x and y where at 
		# least one of the bits is not set 
		x = x ^ y 

		# Carry is shifted by one so that 
		# adding it to x gives the required sum 
		y = carry << 1
	
	return x 

print(Add(15, 32)) 