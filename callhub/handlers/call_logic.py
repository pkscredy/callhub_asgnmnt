from django.core.cache import cache
from callhub.decorators import timeit, recursionlimit
from django.conf import settings
from callhub.dbapi import FibSeriesDbio
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from callhub.constants import MAX_LIMIT
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def cache_dec(num):
    num_result = fibonacci(num)
    cache.set(num, num_result, timeout=CACHE_TTL)
    return num_result


@timeit
def fib_cal(fib_num, memo):
    if memo[fib_num] is not None:
        return memo[fib_num]
    elif fib_num == 1 or fib_num == 2:
        result = 1
    else:
        result = fib_cal(fib_num-1, memo) + fib_cal(fib_num-2, memo)
    memo[fib_num] = result
    cache.set(fib_num, result, timeout=CACHE_TTL)
    return result


def fibonacci(fib_num):
    memo = [None] * (fib_num+1)
    return fib_cal(fib_num, memo)


def retreive_num(num):
    with recursionlimit(MAX_LIMIT):
        fib_obj = FibSeriesDbio().filter_objects({'num_key': num}).last()
        if not fib_obj:
            cache_dec(num)
            fib_obj = FibSeriesDbio().get_object({'num_key': num})
            return {
                'num': fib_obj.num_key,
                'result': fib_obj.result,
                'execution_time': fib_obj.exec_time
            }
        cache.set(fib_obj.num_key, fib_obj.result, timeout=CACHE_TTL)
        return {
            'num': fib_obj.num_key,
            'result': fib_obj.result,
            'execution_time': fib_obj.exec_time
        }
