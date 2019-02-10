import functools
import logging
import time

timestamp = time.time()


def dec_logger(origin_func):
    logging.basicConfig(filename='{}.log'.format(origin_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('{}'.format(origin_func.__name__) + str(args))
        return origin_func(*args, **kwargs)

    return wrapper


def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug


@debug
def add(x, y):
    return x + y


print('Print out - ', add(2,5))
print('Print out - ', add(4,5))


def say_hello(name):
    return f"Hello {name}"

print(say_hello('Meee'))
