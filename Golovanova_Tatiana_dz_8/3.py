import functools


def type_logger(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        args_gen = (f'{a}: {type(a)}' for a in args)
        kwargs_gen = (f'{k}: {v} - {type(v)}' for k, v in kwargs.items())
        args_kwargs_str = f'args: ({", ".join(args_gen)}), kwargs: ({", ".join(kwargs_gen)})'

        result = f(*args, **kwargs)
        print(f'{f.__name__}({args_kwargs_str}) -> {result}: {type(result)}')

        return result
    return wrapper


@type_logger
def test_func(x, y, i, j):
    return [x, y, i, j]


test_func(1, 2.0, i='a', j=None)
