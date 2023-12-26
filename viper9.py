class CustErr(Exception):

    def __str__(self):
        return "custom exception occurred at line 4"


try:
    raise CustErr("Stub!")  # similar to throw in Java

except (CustErr, Exception) as e:
    e.add_note("Error here")
    raise
    # print(e)  # print string representation of exception
    # print(type(e))
    # print(e.args)

    # raise CustErr from e  # from keyword is used to indicate that this exception is a direct cause of e. will help when you read the stack trace

def foo(*, bar):
    pass

foo(bar=4)
reversed([3,4,4])

print(dir(reversed))