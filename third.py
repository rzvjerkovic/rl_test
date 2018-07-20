# Decorator for caching function returns for 10 minutes or 5 calls 
import random
import datetime

time_treshold = 10 * 60
counter_treshold = 5


# Args + kwards hashing func
kw_splitter = object()
def hash_args(args, kwargs):
    return hash(str(args)) + hash(kw_splitter,) + hash(tuple(sorted(kwargs.items())))
    
def cache_returns(func_to_cache):
    args_dict = {}
    def wrapper(*args, **kwargs):
        key = hash_args(args, kwargs)
        # If args not cached, or time and counter passed
        if ((not key in args_dict) or (args_dict[key].counter > counter_treshold) or (time_passed(args_dict[key].start))):
            ret_val = func_to_cache(*args)
            dict_val = DictVal(ret_val)
            args_dict[key] = dict_val
            return ret_val
        # Return cached
        else:
            args_dict[key].increase_counter()
            return args_dict[key].value
            
    return wrapper

# Check time diff from now
def time_passed(start):
    return (datetime.datetime.now() - start).total_seconds() > time_treshold

# Dict cache values
class DictVal:
    def __init__(self, value):
        self.value = value
        self.counter = 0
        self.start = datetime.datetime.now()

    def increase_counter(self):
        self.counter += 1

# Test the method
@cache_returns
def decorator_test(arg, arg2):
    return random.randint(0, 9)

print decorator_test(1, 2, kw = 3)
print decorator_test(1, 2, kw = 3) 
print decorator_test(1, [1, 2, 3])
print decorator_test(1, [1, 2, 3])
