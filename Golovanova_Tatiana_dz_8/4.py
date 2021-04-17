import functools


def val_checker(callback):
    def wrap(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            if not callback(*args, **kwargs):
                raise ValueError(f'wrong val args:{args} kwargs:{kwargs}')
            return f(*args, **kwargs)
        return wrapper
    return wrap


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(5))
calc_cube(-5)
