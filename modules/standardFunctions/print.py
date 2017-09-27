# print
print("- print")
print("\tprints stuff out")
# print(value1, ..., sep=' ', end='\n', file=sys.stdout, flush=False, end="")
print( "Hello","again", sep="|", end=".\n" )
print()

# -- modulus printing
# %[flags][width][.precision]type 
# flags:
#   #   |   Used with o, x or X specifiers the value is preceded with 0, 0o, 0O, 0x or 0X respectively.
#   0   |   The conversion result will be zero padded for numeric values.
#   -   |   The converted value is left adjusted
#       |   If no sign (minus sign e.g.) is going to be written, a blank space is inserted before the value.
#   +   |   A sign character ("+" or "-") will precede the conversion (overrides a "space" flag).
# printing format types (data in tuple will be passed through an appropriate converter to reach these types):
#   d   |   Signed integer decimal.
#   i   |   Signed integer decimal.
#   o   |   Unsigned octal.
#   u   |   Unsigned decimal.
#   x   |   Unsigned hexadecimal (lowercase).
#   X   |   Unsigned hexadecimal (uppercase).
#   e   |   Floating point exponential format (lowercase).
#   E   |   Floating point exponential format (uppercase).
#   f   |   Floating point decimal format.
#   F   |   Floating point decimal format.
#   g   |   Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
#   G   |   Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
#   c   |   Single character (accepts integer or single character string).
#   r   |   String (converts any python object using repr()).
#   s   |   String (converts any python object using str()).
#   %   |   No argument is converted, results in a "%" character in the result.

print( "the value is %i. this value is %.2f" % (2, 30.14159) )
print("look at all these values")
print("x: %5i" % 122)
print("x: %5i" % 0)
print("x: %5i" % 15462)
print("x: %5i" % 6546)
print("x: %5i" % 12)
print("x: %5.2f" % 0.876543)

s = "x: %5.2f" % 0.876543
print( s )

print()

# -- string method format
# addition, pre-formatting formatting
#   <   |   The field will be left-aligned within the available space. This is usually the default for strings.
#   >   |   The field will be right-aligned within the available space. This is the default for numbers.
#   0   |   If the width field is preceded by a zero ('0') character, sign-aware zero-padding for numeric types will be enabled.
#   ,   |   This option signals the use of a comma for a thousands separator.
#   =   |   Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form "+000000120". This alignment option is only valid for numeric types.
#   ^   |   Forces the field to be centered within the available space.
#   +   |   indicates that a sign should be used for both positive as well as negative numbers.
#   -   |   indicates that a sign should be used only for negative numbers, which is the default behavior.
#    	|   indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.

print( " {} {} {} ".format(1,2,3) )
print( " {0} {0} {1} ".format(100,1) )
print( " {a} {b} {b} ".format(a=100,b=1) )
print( "the value is {1:.2f}. this value is {0:d}".format(2, 30.14159) )
print()

#   in conjunction with a dictionary
capital_country = {"United States" : "Washington", 
                   "US" : "Washington", 
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    print("\t"+c+": {capital}".format(capital=capital_country[c]))
print()