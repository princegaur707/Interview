def Add(x, y): 
    while (y != 0): 
	    # carry now contains common 
		# set bits of x and y 
        carry = x & y 
        print("carry:",carry)

		# Sum of bits of x and y where at 
		# least one of the bits is not set 
        x = x ^ y 
        print("x:",x)

		# Carry is shifted by one so that 
		# adding it to x gives the required sum
        y = carry << 1
        print("y:",y)
    return x
print(Add(15, 15)) 

# #Recursive solution
# int Add(int x, int y) 
# { 
# 	if (y == 0) 
# 		return x; 
# 	else
# 		return Add( x ^ y, (x & y) << 1); 
#} 
