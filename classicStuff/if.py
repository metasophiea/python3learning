if True:
    print("Hello")

string = "Hello"
string_2 = "Hello"
if string == string_2:
    print("Hello again")

word = input("enter input:")
if word == "input":
    print("wise guy")
elif word == "ok":
    print("Hello")
else:
    print("elsed")


# ternary version
number = 10 if (string == word) else 100
print(number)
number = 2 * (10 if (string == word) else 100)
print(number)
# they act like a sub function in this way