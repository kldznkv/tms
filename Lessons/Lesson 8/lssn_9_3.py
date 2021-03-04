import time

def calc_time(func):
    def wrap():
        start_at = time.time()
        func(n)
        end_at = time.time()
        print(f"{end_at - start_at }")
    return wrap

@calc_time
def long():
    for _ in range(n):
        pass

long(n)





