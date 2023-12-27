import sys


if __name__ == '__main__':

    print("*** I'LL TELL YOU WHAT THE CO-ORDINATES ARE IN THE CARTESIAN PLANE ***")

    class Coordinate:
        x: int
        y: int

        def __init__(self, x, y):
            self.x = int(x)
            self.y = int(y)

    coord_x = sys.argv[1]
    coord_y = sys.argv[2]

    coord = Coordinate(coord_x, coord_y)
    coord_tuple = (int(coord_x), int(coord_y))

    match coord:
        case Coordinate(x=0, y=0):
            print("coordinate is at origin")
        case Coordinate(x=coord_x, y=0):
            print(f"equation of horizontal line through x is x={coord_x}")
        case Coordinate(x=0, y=coord_y):
            print(f"equation of vertical line through y is y={coord_y}")
        case Coordinate(x=a, y=b) if a == b:
            print("coordinate x and y values are the same")
        case _:
            print("coordinate is lost somewhere in the expanse of the cartesian plane")

    match coord_tuple:
        case (0, 0):
            print("coordinate is at origin")
        case (coord_x, 0):
            print(f"equation of horizontal line through x is x={coord_x}")
        case (0, coord_y):
            print(f"equation of vertical line through y is y={coord_y}")
        case (e, f) if e == f:
            print("coordinate x and y values are similar")
        case _:
            print(f"coordinate is lost somewhere in the expanse of the cartesian plane")
