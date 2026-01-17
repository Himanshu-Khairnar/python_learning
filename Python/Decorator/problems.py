import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time of {func.__name__}: {end - start} seconds")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(2)


def dec(func):
    def wrapper(*args, **kwargs):
        args_join = ", ".join(str(arg) for arg in args)
        kwargs_join = ", ".join(f"{k}: {v}" for k, v in kwargs.items())
        print(
            f"Function Name: {func.__name__} \nargs: {args_join or "nothing"} \nkwargs: {kwargs_join or "nothing"} "
        )
        result = func(*args, **kwargs)
        return result

    return wrapper


@dec
def greet(name, greeting="hello"):
    print(f"{greeting}, {name}")


@dec
def hello():
    print("hello")


# hello()
# greet("chai",greeting="hanji ")


def cache(func):
    cache_value = {}
    print("Cache initialized ",cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result

    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2,3))
print(long_running_function(2,3))
print(long_running_function(5,3))