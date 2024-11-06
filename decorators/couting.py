import functools

def count_calls(func):
    @functools.wraps(func)  # Preserva metadados da função original
    def wrapper(*args, **kwargs):
    
        wrapper.calls += 1
        print(f"A função '{func.__name__}' foi chamada {wrapper.calls} vezes")
        
        
        return func(*args, **kwargs)
    
    # Inicializa o contador de chamadas como um atributo da função wrapper
    wrapper.calls = 0
    return wrapper

