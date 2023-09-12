# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple
Point = collections.namedtuple("Point", "x y")
p = Point(1, 3)
print(p)
print(p.x, p.y)

# TODO: use _replace to create a new instance
p = p._replace(x=100)
print(p)
