import traceback
from typing import Protocol, List, Callable


code = '''
class Foo:
    def __init__(self, x):
        self.x = x
    def get(self):
        return self.x

f = Foo(100)
foo = lambda x: x + f.get()
'''


class TestIt:

    def __init__(self, code: str) -> None:
        self.code = code
        self.namespace = {}
        exec(self.code, self.namespace)

    def test(self) -> bool:
        fn = self.namespace.get('foo')
        try:
            x = 'str'
            x ** 10
            print(fn(100))
            assert fn(5) == 10000
            return True
        except:
            # print(traceback.format_exc())
            print('last line')
            last_line = traceback.format_exc().splitlines()[-1]
            print(last_line)
            return False


if __name__ == '__main__':
    ti = TestIt(code=code)
    result = ti.test()
