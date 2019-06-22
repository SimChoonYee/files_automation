def test1():
    class test:
        def __init__(self):
            self._x = None

        @property
        def x(self):
            return self._x

        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self, ):
            del self._X


def test2():
    # Data descriptors > Normal attributes > non data descriptors
    class Klass:
        '''
        https://www.thebookofjoel.com/blog/python-data-descriptors
        A handy shortcut to creating a data descriptor out of a method is with the @property decorator.
        This will make the decorated function a data descriptor even if you don't have a setter defined,
        meaning that it will always take precedence over attribute lookup in the object __dict__.
        '''

        @property
        def x(self):
            return 5

    klass = Klass()
    print(klass.x)  # running method x
    print(klass.__dict__)

    print('\n')
    klass.y = 8  # setting normal attributes
    print(klass.y)
    print(dir(klass.y))
    print(klass.__dict__)
    # print(dir(klass))
    klass.__dict__['y'] = 7  # same as assign normal attribute for y. avoid say setting cause we have setter
    print('space')
    print(klass.y)  # It overrides that normal attr y since setter is defined
    print(dir(klass.y))
    print(klass.__dict__)
    print('\n')

    print('end of y')
    try:
        klass.x = 7  # setter for x is declared but not defined
    except Exception as e:
        print(e)
    klass.__dict__['x'] = 7
    print(klass.__dict__)
    print(klass.x)  # since this is a data descriptor the __dict__ lookup is overridden

def test3():
    class ExDescriptors:
        def __get__(self, instance, owner):
            return 5

    class Klass:
        x = ExDescriptors()

    klass = Klass()  # klass is non data descriptors
    print(klass.x)
    klass.x = 7
    print(klass.x)  # print normal attr of x OR __dict__['x']
    del klass.x
    print(klass.x)

if __name__ == "__main__":
    test3()
