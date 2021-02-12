import pandas as pd

data_tokped_csv = pd.read_csv('ws_user.csv')

data_tokped = data_tokped_csv.to_dict('Records')

def lowercase(func):
  def wrapper():
    func_ret = func()
    change_to_lowercase = func_ret.get()
    return change_to_lowercase
  return wrapper

#%%
#testing 1
def hello_function():
  return 'HELLO WORLD'

decorate = lowercase(hello_function)
print(decorate())

#%%
#testing 2
@lowercase
def hello_function():
  return 'HELLO WORLD'

print(hello_function())

#%%
#multiple decorator
def split_setence(func):
    def wrapper():
        func_ret = func()
        output = func_ret.split()
        return output
    return wrapper

#%%
#testing 3
@split_setence
@lowercase
def hello_function():
    return 'HELLO WORLD'

print(hello_function())

#%%
#memoization using decorator
#Cache value
import functools
def memoize(function):
    function.cache = dict()
    @functools.wraps(function)
    def __memoize__(*args):
        if args not in function.cache:
            function.cache[args] = function(*args)
        return function.cache[args]
    return __memoize__

#%%
#testing 4
@memoize
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(1, 7):
    print('fibonacci %d: %d' % (i, fibonacci(i)))

#%%
#LRU Cache
import functools
def counter(function):
    function.calls = 0
    @functools.wraps(function)
    def __counter__(*args, **kwargs):
        function.calls += 1
        return function(*args, **kwargs)
    return __counter__

#%%
#testing 5
@functools.lru_cache(maxsize=3)
@counter
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))

#%%
