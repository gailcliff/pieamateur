class Integr:

    integer: int

    def __init__(self, integer):
        self.integer = integer

    def __str__(self):
        return str(self.integer)


class ZeroDivisionException(Exception):

    def __str__(self):
        return "Division by Zero !.!"


class Calculator:
    a: Integr
    b: Integr

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def divide(self):
        if self.b.integer == 0:
            raise ZeroDivisionException

        return Integr(self.a.integer // self.b.integer)


calc = Calculator(Integr(5), Integr(0))

try:
    result = calc.divide()
except ZeroDivisionException as e:
    print(e)
    print(type(e))
    print(e.args)
    # e.add_note('Division by 0 results in infinite numbers')
    # raise
else:
    print(result)
finally:
    print("Finished computation")


with open('test_file.txt', '+') as f:
    f.write("\nfoobar")
    f.flush()

print(f.closed)
