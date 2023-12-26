import os


def path(foo):
    return foo, ':', os.environ.get('PYTHONPATH')
