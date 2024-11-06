import functools

def loop(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = None
            for i in range(n):
                print(f"\nExecução {i + 1} de {n}")
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator