import sys
from typing import Callable


subscribers = 0


def on_subscribed(user_id: int):
    print(f"adding #{user_id} to subscribers db")


def subscribe(first_name: str, last_name: str, on_subscribe: Callable):
    print(f"signed up {first_name} {last_name}")

    global subscribers

    on_subscribe(subscribers)
    subscribers += 1


# if __name__ == '__main__':
    subscribe("gail", "cliff", on_subscribed)
    subscribe("odhis", "nyanga", on_subscribed)

    def create_subscribe_callback(inner='inner1'):
        def on_user_subscribed(user: int):
            print("called from", inner)
            print(f"onboarded {user} ({subscribers+1} to subscribe)")

        return on_user_subscribed

    subscribe_callback = create_subscribe_callback()
    subscribe_callback(34)
    subscribe("otieno", "aduol", subscribe_callback)

    # subscribe using decorators

    def subscribe_user(user_name: Callable):
        print(f"subscribed user: {user_name()}")

        global subscribers
        subscribers += 1
        subscriber_id = user_name() + f"#{subscribers}"
        return lambda: subscriber_id

    def register_user(details):
        first_name = details()[0]
        last_name = details()[1]

        print(f"registering user (First Name: {first_name}, Last Name: {last_name})")

        return lambda: f"{first_name}_{last_name}"

    @subscribe_user
    @register_user
    def subscriber_id():
        return sys.argv[1], sys.argv[2]

    print(subscriber_id())


# lil mockup of fastapi
if __name__ == '__main__':
    import app
    import sys

    request_type = sys.argv[1]

    @app.post
    def post_user(request: str):
        return request

    @app.get
    def get_user(request: str):
        return request

    @app.put
    def update_user(request: str):
        return request


    @app.delete
    def delete_user(request: str):
        return request


    req = sys.argv[2]

    match request_type:
        case 'GET':
            print(get_user(req))
        case 'POST':
            print(post_user(req))
        case 'PUT':
            print(update_user(req))
        case 'DELETE':
            print(delete_user(req))
        case _:
            raise Exception("Invalid Request")
