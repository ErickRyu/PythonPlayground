import logging
import time

timestamp = time.time()


def dec_logger(origin_func):
    logging.basicConfig(filename='{}.log'.format(origin_func.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('{}'.format(origin_func.__name__) + str(args))
        return origin_func(*args, **kwargs)

    return wrapper


@dec_logger
def add(x, y):
    return x + y


print(add(2,5))
print(add(4,5))
