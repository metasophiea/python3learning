# the lead file of a package
# the code here will be run once after the package is imported
print("Hello from simplePackageExample __init__.py")

# the following code automatically imports the submodules into execution
import simplePackageExample.submodule_a
from . import submodule_b # here we see one can use the file system to import what we like, in affect allowing one to import code for other parts of the package (from subfolders or subsections of a package)