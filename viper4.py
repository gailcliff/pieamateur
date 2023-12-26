
def greet(greeting, /, first_name, *, last_name='Doe'):
    print(greeting, first_name, last_name)


def power(num, power):
    return num ** power


def foo(*args, **kwargs):
    for arg in args: print(arg, end=' ')
    print()
    for kwarg in kwargs: print(f'{kwarg}: {kwargs[kwarg]}', end=', ')
    print()


def signup_user(fname: str, lname: str, oname=''):
    print("signing up user...")
    print(f"signed up user with username {fname}_{lname} {oname}")
    return {"user_id": 42}


def fetch_user_data():
    return {
        "fname": 'Gail',
        "lname": 'Cliff',
    }


def exponen(base):
    return lambda power: base ** power


def is_user_siged_up(username: str, pin: int) -> bool:
    return False


if __name__ == '__main__':
    dat = fetch_user_data()
    names = ('luc', 'man')
    signup_user(**dat)
    signup_user(*names)

    power_up = exponen(2)
    print(power_up(4))
    print(power_up(8))
    print(power_up(5))
    print(is_user_siged_up('user', 65))


__all__ = ['is_user_siged_up', 'signup_user', 'power']