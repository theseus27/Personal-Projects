import datetime
import time

#EXAMPLE 1 ()
def day_only(func):
    def wrapper():
        if 7 <= datetime.datetime.now().hour < 22:
            print("It's day time!")
            func() 
        else:
            print("It's night time.")
    return wrapper

def hello():
    print("Hi!")

#Call 1
hello = day_only(hello)
hello()

#Call 2
@day_only
def pokemon():
    print("Pokemon is awesome!")
pokemon()

#EXAMPLE 2
def take_args(func):
    def wrapper(*args):
        print("You called function: " + str(func.__name__))
        return func(*args)
    return wrapper

@take_args
def print_names(*names):
    return names[1]
        
returned = print_names("Luke", "Jimmy", "Marco")
print(returned)

#EXAMPLE 3 (Timer Wrapper)
def timer(func):
    def wrapper_timer(*args):
        start_time = time.perf_counter()
        returned = func(*args)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"{func.__name__} finished in {run_time:.4f} seconds.")
        return returned
    return wrapper_timer

@timer
def time_waster(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

time_waster(100)

#EXAMPLE 4 (Debugging)
import functools
def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_representation = [repr(a) for a in args]                      # 1
        
        kwargs_representation = [f"{key}={value!r}" for key, value in kwargs.items()]  # 2
        
        signature = ", ".join(args_representation + kwargs_representation)           # 3
        
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def greeting(name, age=20):
    return f"Hi {name}, you are {age} years old!"

greeting("Theseus")