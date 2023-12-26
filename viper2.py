
class Coordinate:
    I: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y


i = int(input("Enter x co-ordinate:\t"))
j = int(input("Enter y co-ordinate:\t"))

coord = Coordinate(i, j)
coord_tuple = (i, j)
coords = [Coordinate(i, j), Coordinate(j, i)]

match coords:
    case [Coordinate(x=a1, y=0), Coordinate(x=y1, y=0)]:
        print("Two points along the y-axis")
    case _:
        print("none or one on y")


match coord_tuple:
    case (0, 0):
        print("origin")
    case (0, y):
        print(f'y={y}')
    case (x, 0):
        print(f"x={x}")
    case (e, f):
        print(f"at ({e}, {f})")
    case _:
        print("idk")


match coord:
    case Coordinate(x=a, y=b) if a == b:
        print("x and y of coord are the same")
    case Coordinate(x=0, y=0):
        print("coord is at origin")
    case Coordinate(x=0, y=y):
        print(f"coord is at the line y={y}")
    case Coordinate(x=d, y=0):
        print(f"coord is at the line x={d}")
    case Coordinate(x=a, y=b):
        print(f"coord is at ({a}, {b})")
    case _:
        print("delusional")

