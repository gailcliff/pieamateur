# from spin import *
from fad.baz import chaz, daz
from fad import chad
# import fad.baz.chaz.loo
import fad.baz
import json

# fad.baz.daz()

chad.chaddy_boy()
chaz.loo()
daz()


def foo(bar, /, baz, *, chaz):
    """Restricting how function arguments can be passed in"""
    print(bar, baz, chaz)


foo(4, "fasd", chaz=True)
len([])
print([5,6,4,34,6,2].index(4,-300))

print(set("thequickbrownfoxesjumpedoverthelazydogs"))

help(foo)


class Foo:
    a: int
    b: str

    def __init__(self, a, b):
        self.a = a
        self.b = b


foo = Foo(12, "foobar")

foo_str = json.dumps(foo.__dict__, indent=2)
print(foo_str)

foo_json = json.loads(foo_str)
print(foo_json)

print(foo_json['a'])
print(foo.b)

from datetime import datetime

print(datetime.now().microsecond)


