import time

def timecalc(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        result = func(*args, **kwargs)
        et = time.time()
        print(f"Time required to execute the program {et - st}")
        return result
    return wrapper
        
@timecalc
def greet(name = 'world'):
    return f"Hello {name}"


print(greet("Himanshu"))

"""
output-

Time required to execute the program 1.9073486328125e-06
Hello Himanshu

"""