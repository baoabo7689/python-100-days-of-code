# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args, **kwargs):
        params = ", ".join(map(str, args))
        result = function(*args, **kwargs)
        print(f"You called {function.__name__}({params})\nIt returned: {str(result)}")
        return result
    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
decorated_a_function = logging_decorator(a_function)
decorated_a_function(1,2,3)