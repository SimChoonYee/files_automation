def test1():
    from debugEx import printName

    @printName
    def add2Num(x, y):
        # add two numbers
        # print("add")
        return (x + y)

    print(add2Num(2, 4))
    help(add2Num)


def test2():
    # mathEx.py

    from debugEx import printName

    @printName('**')
    def add2Num(x, y):
        '''add two numbers'''
        return (x + y)

    print(add2Num(2, 4))
    # help(add2Num)

def test3():
    from debugEx import printName

    @printName(prefix='**')
    def add2Num(x, y):
        '''add two numbers'''
        return (x + y)

    @printName
    def diff2Num(x, y):
        '''subtract two integers only'''
        return (x - y)

    print(add2Num(2, 4))
    print(diff2Num(2, 4))
    # help(add2Num)

if __name__ == "__main__":
    test2()
