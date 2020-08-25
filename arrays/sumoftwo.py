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

#Recursive solution
int Add(int x, int y) 
{ 
	if (y == 0) 
		return x; 
	else
		return Add( x ^ y, (x & y) << 1); 
} 
