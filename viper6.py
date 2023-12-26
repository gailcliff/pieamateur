import viper4
from pprint import pp
from viper4 import *

import sys
import builtins

import fad.baz


user_id = signup_user(fname='john', lname='doe')

# print(user_id['user_id'])
#
# print(__name__)
# print(sys.builtin_module_names)
# print(sys.path)
#
# pp(dir(builtins))
# print(power(4,4))

fad.baz.daz()
