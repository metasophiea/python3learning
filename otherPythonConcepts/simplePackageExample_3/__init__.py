# the lead file of a package
# the code here will be run once after the package is imported
print("Hello from simplePackageExample_3/__init__.py")

# this variable should contain all the subpackages and modules to be imported when someone writes "from [package] import *"
__all__ = ["submodule_a", "submodule_b"]