# while

counter = 0
while counter < 10:
    print( str(counter) + " : Hello")
    counter += 1
print()

#  breaks and else
# a break statement will end the loop, skipping the else code, which is 
# only run when the 'while' condition resolves to false
counter = 0
while counter < 10:
    print( str(counter) + " : Hello")
    if counter == 90:
        break
    counter += 1
else:
    print("else opperations")

print("post loop")
print()

# continue
# a continue statement will restart the loop (doing the judgement at the top)
counter = 0
while counter < 10:
    counter += 1
    if counter == 5:
        continue
    print( str(counter) + " : Hello")

print("post loop")
print()
print()

# for
#    for <variable> in <sequence>:
#        <statements>
#    else:
#        <statements>

languages = ["Java", "C++", "JavaScript", "Python"] 
for x in languages:
    print(x)
print()

# for loops also have the 'break','continue' and 'else' functionality
edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        continue
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")
print()

# using ranges
for x in range(0,10):
    print(x)
print()

list = ["Java", "C++", "JavaScript", "Python"]
for x in range(len(list)):
    print(x,list[x])
print()


# enumeration
aList = ["ham", "spam","eggs","nuts"]
for index,item in enumerate(aList):
    print(index,item)
print()