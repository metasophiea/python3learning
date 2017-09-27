val = int(5)            # val    = 5   
print(val)

binVal = bin(10)        # binVal = 0b1010
print(binVal)

octVal = oct(10)        # octVal = 0o12
print(octVal)

hexVal = hex(10)        # hexVal = 0xa
print(hexVal)

compVal = 5 + 1j 
print(compVal)

multVal = 5 * 2
print( multVal )

modVal = 5 % 2
print( modVal )

fractVal = 1/12
print(fractVal)

floorFractVal = 1//12
print(floorFractVal)

expVal = 5 ** 2
print( expVal )

bitNegVal = ~5
print( bitNegVal )

leftShiftval = 5 << 1
print( leftShiftval )

rightShiftval = 5 >> 1
print( rightShiftval )


print()

a = 300
b = 300
print( a is b )
print(id(a) , id(b))
# python saves on memory by making two pointers that point 
# to identical objects, point to the same object