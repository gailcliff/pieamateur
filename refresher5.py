# import app
from app import test, Test


@test('/cliff')
def foo():
    return "bar"


if __name__ == '__main__':
    print(foo)

    test = Test('grep')
    print(test.test_name)

