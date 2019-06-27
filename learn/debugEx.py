# def printName(func):
#     # func is the function to be wrapped
#     def pn(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#     return pn
#
#
# # debugEx.py

# test1
# from functools import wraps
#
# def printName(func):
#     # func is the function to be wrapped
#
#     # wrap is used to exchange metadata between functions
#     @wraps(func)
#     def pn(*args, **kwargs):
#         print(func.__name__)
#         return func(*args, **kwargs)
#     return pn

# test2
from functools import wraps

def printName(prefix=""):
    def addPrefix(func):
        msg = prefix + func.__name__
        # func is the function to be wrapped

        # wrap is used to exchange metadata between functions
        @wraps(func)
        def pn(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return pn
    return addPrefix

# test3
# debugEx.py

# from functools import wraps, partial
#
# def printName(func=None, *, prefix=""):
#     if func is None:
#         return partial(printName, prefix=prefix)
#     # wrap is used to exchange metadata between functions
#     @wraps(func)
#     def pn(*args, **kwargs):
#         print(prefix + func.__name__)
#         return func(*args, **kwargs)
#     return pn