import simplePackageExample

print()

# running a specific import like this, actually runs the __init__.py files for every level
# in this example, simplePackageExample_2/subsection_1/__init__.py indicates that the sub
# package subsection_2 is required, so that is imported (running it's __init__.py file)
# once all that is complete and the simplePackageExample_2/subsection_1/__init__.py is
# finished; then the module we requested is actually imported
import simplePackageExample_2.subsection_1.subsectionModule

print()

from simplePackageExample_3 import *

print()
print( dir() )
simplePackageExample.submodule_a.bar()
print()
simplePackageExample_2.subsection_1.subsectionModule.test()
simplePackageExample_2.subsection_1.subsection_2.subsectionModule.test()
print()
submodule_a.hello()
submodule_b.fip()