def some_decorator(original_function):
    def decorated_function():
        print("deprecation warning!")
        original_function()
    return decorated_function

@some_decorator
def foo():
    print("foo!!")

foo()