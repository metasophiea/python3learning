import re

# regex raw string
# here, no string-based escaping is necessary
x = r"[1-9]"

# basic matching of a string (only checks the very start of a string)
print( re.match("cat","A cat and a rat can't be friends.") )
print( re.match("cat","cat and a rat can't be friends.") )
# basic searching of a string (checks the entire string)
print( re.search("cat","A cat and a rat can't be friends.") )
print( re.search("cow","A cat and a rat can't be friends.") )
# using search to check only the start and end of a string
print( re.search("^cat","cat and a rat can't be friends.") )
print( re.search("cat$","A cat and a rat can't be friends cat") )
# search multiline (here, the rules will be applied separately for each line)
print( re.search("^cat","A cat and a rat can't be friends.\ncat",re.MULTILINE) )
print()


# match object (the object returned by these functions)
mo = re.search("([0-9]+)", "Customer number: 232454, DateCode: 12022011, ShippingID: 98765")
print(mo)
print( mo.group() )    # the matched string
print( mo.span()  )    # the start and end point of the matched string (as tuple)
print( mo.start() )    # the start point of the matched string
print( mo.end()   )    # the end point of the matched string
print()

# capturing groups
mo = re.search("([0-9]+).+ ([0-9]+).+ ([0-9]+).+", "Customer number: 232454, DateCode: 12022011, ShippingID: 98765")
print(mo)
print( mo.group() )    # the matched string
print( mo.group(1) )   # the first matched string subsection
print( mo.group(2) )   # the second matched string subsection
print( mo.group(3) )   # the third matched string subsection
print( mo.group(1,3) ) # two matched string subsections
print()

# Backreferencing 
# useful for refering to groups within a regex expression
# - numbered
res = re.search(r"<([a-z]+)>(.*)</\1>", "<composer>Wolfgang Amadeus Mozart</composer>") # here, '\1' refers to the first group, thus it's a short hand for "<([a-z]+)>(.*)</([a-z]+)>" though this would capture the closing tag as a separate group
print(res.group(1) + ": " + res.group(2))
# - named
res = re.search(r"<(?P<tag>[a-z]+)>(?P<name>.*)</(?P=tag)>", "<composer>Wolfgang Amadeus Mozart</composer>")
print(res.group("tag") + ": " + res.group("name"))
print()


# wildcard searching .
print( re.search(".at","This will match any segment that contains the letters 'a' and 't' preceded by any character") )
# optional items (and grouping(subexpressions)) ()?
print( re.search("Feb(ruary)?","This will match the strings of Feb and February") )
# repeat characters *
print( re.search("[0-9][0-9]", "This will match an arbitrary number of number characters, not just a single character from a number 2345. Importantly, that arbitrary number can be zero hence the double [0-9]") )
print( re.search("[0-9][0-9]*","This will match an arbitrary number of number characters, not just a single character from a number 2345. Importantly, that arbitrary number can be zero hence the double [0-9]") )
# repeat characters (at least one) +
print( re.search("[0-9]+","This will match an arbitrary number of number characters from this string 2345") )
# repeat characters (to/from) {}
print( re.search("[0-9]{3}","This will match an 3 number charactersfrom this string 2345") )
print( re.search("[0-9]{2,}","This will match an numbers with at least 2 numerical characters from this string 2345") )
print( re.search("[0-9]{,2}","This will match an numbers with at most 2 numerical characters from this string 2345 (this includes 0 characters)") )
print( re.search("[0-9]{1,2}","This will match an numbers with between 1 and 2 numerical characters from this string 2345") )


# Character Classes []
print( re.search("Br[ae]ndon","This will match any spelling of the classic name 'Brandon'") )
# - dash -
# dashes only represent "this to that" when they are not beside a square bracket
print( re.search("[A-Z]","this will match any Upper case letter") )
print( re.search("[-yz]","this will match the dash character along with the two letters -") )
# - caret ^
# carets only work as NOT operators when they are the first character after a square bracket
print( re.search("[^A-Z]","this will match anything but Upper case letter") )
print( re.search("[A-Z^]","this will match any Upper case letter along with a caret") )
# - Predefined Character Classes
# \b    Matches a word boundary, which is the start and end of any sequency of alphanumeric characters
# \B    Compliment of \b
# \d	Matches any decimal digit; equivalent to the set [0-9].
# \D	The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].
# \s	Matches any whitespace character; equivalent to [ \t\n\r\f\v].
# \S	The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
# \w	Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]. With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.
# \W	Matches the complement of \w.
# \\	Matches a literal backslash.
# Alternation - matching whole strings
print( re.search("(london|paris)","dublin london") )
print()

# findall - re.findall(pattern, string[, flags])
# this returns a list of non-overlapping matches of pattern in the string
t = "A fat cat doesn't eat oat but a rat eats bats."
mo = re.findall("[force]at", t)
print(mo)
# grouping in the expression, returns a list of tuples
courses = "Python Training Course for Beginners: 15/Aug/2011 - 19/Aug/2011;Python Training Course Intermediate: 12/Dec/2011 - 16/Dec/2011;Python Text Processing Course:31/Oct/2011 - 4/Nov/2011"
print( re.findall("([^:]*):([^;]*;?)", courses) )
print()

# compile - re.compile(pattern[, flags])
# one can compile a regex expression into an object for faster execution (though apparently not that much faster)
regex = r"[A-Z]"
compiled_regex = re.compile(regex)
print( compiled_regex.search("this will match any Upper case letter") )
print()

# split
# does the same job as the string objects split method, but with regex
print( re.split("\W+","A big long and very important string") ) #standard whitespace split
print( re.split("(big|very)","A big long and very important string") ) #spliting on words
print()

# sub - re.sub(regex, replacement, string)
# for every match, the replacement string is substituted in
print( re.sub("[yY]es","no", "yes I said yes I will Yes.") )
print()