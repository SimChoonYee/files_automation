def plus(x):
    x = x + 1
    return x


def str_if_None(*args):
    # y = 10
    # x = plus(x)
    # print(x)
    # return (y, x if x else "")
    for arg in args:
        if arg:
            return arg
        else:
            return ""


res, res2 = str_if_None('a')
print(res)
print(res2)
# def myfunc(a, b):
#   return a + b
#
# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# y = map(myfunc, ('cherry'), ('pineapple'))
# print(y)
#
# #convert the map into a list, for readability:
# print(list(x))
