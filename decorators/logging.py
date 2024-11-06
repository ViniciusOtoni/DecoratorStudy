import functools

def log_decorator(func):
    @functools.wraps(func)  # Preserva metadados da função original
    def wrapper(*args, **kwargs):
        # Chamada da função e seus args
        print(f"Chamando a função '{func.__name__}' com argumentos {args} e {kwargs}")
        
        
        res = func(*args, **kwargs)
        
        # Loga o resultado da função
        print(f"'{func.__name__}' retornou {res}")
        
        return res
    return wrapper

