def trace(func):
    def traced():
        print("Trace: {0} ({1}:{2})"
            .format(func.__name__,
                    func.__code__.co_filename,
                    func.__code__.co_firstlineno))
        return func()
    return traced

@trace
def foo():
    print("foo!")

foo()