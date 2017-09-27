print("Hello from simplePackageExample_2/subsection_1/__init__.py")

# this sub package for some reason needs subsection_2 in order to work, so we can import that
print("i need subsection_2")
from .. import subsection_2