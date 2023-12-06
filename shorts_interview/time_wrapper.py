from datetime import datetime

def func_wrapper_time(func):
    def wrapper(*arg, **kwarg):
        start = datetime.now()
        result = func(*arg, **kwarg)
        delta_time = datetime.now() - start
        print(f"Execution time: {delta_time}")
        return result
    return wrapper


import time

@func_wrapper_time
def func_1():
    time.sleep(1)

@func_wrapper_time
def func_2():
    time.sleep(2)

func_1()
func_2()
