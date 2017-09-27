name = input("What is your name? ")
print("Hello " + name)

eval(input("I'll eval this for you " + name + ": "))

# direct access
import sys
character = sys.stdin.read(1)
print( character )

sys.stdout.write("Hello\n")

sys.stderr.write("Hello\n")