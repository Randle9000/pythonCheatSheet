import simple_package

print(simple_package)

#####################

from simple_package import a, b
a.bar()
b.foo()

####################

import simple_package.a
simple_package.a.bar()