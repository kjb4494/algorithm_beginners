import time


def time_measurement(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        order = func(*args, **kwargs)
        print('--- {} seconds ---'.format(time.time() - start_time))
        return order

    return wrapper
