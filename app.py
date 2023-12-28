from typing import Callable
from dataclasses import dataclass


def get(fn: Callable):
    return lambda request: fn({"GET": f"{request}"})


def post(fn: Callable):
    return lambda request: fn({"POST": f"{request}"})


def put(fn: Callable):
    return lambda request: fn({"PUT": f"{request}"})


def delete(fn: Callable):
    return lambda request: fn({"DELETE": f"{request}"})


def test(token: str):
    return lambda x: f"parsed: {token}"


@dataclass
class Test:
    test_name: str
