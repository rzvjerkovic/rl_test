# Decorator for caching function returns for 10 minutes or 5 calls 
import random
import datetime

time_treshold = 10 * 60
counter_treshold = 5

def cache_returns(func_to_cache):
    args_dict = {}
    def wrapper(*args, **kwargs):
        key = hash_args(args, kwargs)
        # Check is args are in dict and if tresholds pass
        if key in args_dict and args_dict[key].calls != counter_treshold and !time_passed(args_dict[key].start):
            args_dict[key].increase_counter()
            return args_dict[args]
        # If not, recalculate. Reset tresholds
        else:
            ret_val = func_to_cache(*args)
            dict_val = DictVal(ret_val)
            args_dict[key] = dict_val
            return ret_val
    return wrapper

# Args + kwards hashing func
def hash_ags(args, kwargs):
    kw_splitter = object()
    return args + (kw_splitter) + tuple(sorted(kwargs.items))

# Check time diff from now
def time_passed(start):
    return (datetime.datetime.now() - start).total_seconds() > time_treshold

class DictVal:
    def __init__(self, value):
        self.value = value
        self.counter = 0
        self.start = datetime.datetime.now()

    def increase_counter(self):
        self.counter++

@cache_returns
def decorator_test(arg, arg2):
    return random.randint(0, 9)

decorator_test(1, 2, 3, kw = 3)
decorator_test(1, 2, 4, kw = 3) 
decorator_test(1, 2)
decorator_test(1, 2)
