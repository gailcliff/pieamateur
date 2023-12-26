from typing import Callable


def on_signed_up(user_id: int, username: str):
    print(f"{username} was signed up with id {user_id}")


def signup_user(fname, lname, on_signup: Callable):
    username = '_'.join((fname, lname))
    on_signup(743, username)


signup_user('gail', 'cliff', on_signed_up)

signup_user = 4

print(type(signup_user))


def fn_to_upper_case(fn: Callable):
    return lambda: fn().upper()


def fn_split_string(fn: Callable):
    return lambda: fn().split()  # split the string to a list


@fn_split_string
@fn_to_upper_case  # the decorators are executed from the bottom to up. the last decorator gets executed first.
                   # in this case when you apply the decorators the other way round it won't work because lists don't have an upper() method
def go_big():
    return 'go big gail cliff'


print(go_big())

# More info on decorators: https://www.datacamp.com/tutorial/decorators-python