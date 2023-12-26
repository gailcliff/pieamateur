from enum import Enum


class Color(Enum):
    RED = True
    GREEN = True
    BLUE = True


# color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))
color = Color(True)
match color:
    case Color.GREEN:
        print("I see GRE!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")