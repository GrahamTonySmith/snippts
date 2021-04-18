"""Chain of responsibility"""


from abc import ABC, abstractmethod
from typing import Optional, Any



class Handler(ABC):

    def __init__(self, sucessor=None):
        self._sucessor = sucessor

    def set_sucessor(self, handler: 'Handler'):
        self._sucessor = handler
        return handler

    @property
    def clsname(self):
        return self.__class__.__name__

    @abstractmethod
    def handle(self, request):
        pass


class ConcreteHandler1(Handler):

    def handle(self, request):
        if request == 1:
            print(f"{self.clsname} handled request: {request}")
        elif self._sucessor:
            self._sucessor.handle(request)
        else:
            print(f"request: {request} unhandled")


class ConcreteHandler2(Handler):

    def handle(self, request):
        if request == 2:
            print(f"{self.clsname} handled request: {request}")
        elif self._sucessor:
            self._sucessor.handle(request)
        else:
            print(f"request: {request} unhandled")


class ConcreteHandler3(Handler):

    def handle(self, request):
        if request == 3:
            print(f"{self.clsname} handled request: {request}")
        elif self._sucessor:
            self._sucessor.handle(request)
        else:
            print(f"request: {request} unhandled")


if __name__ == '__main__':
    h1 = ConcreteHandler1()
    h2 = ConcreteHandler2()
    h3 = ConcreteHandler3()
    
    h1.set_sucessor(h2).set_sucessor(h3)

    h1.handle(1)
    h1.handle(2)
    h1.handle(3)
    h1.handle(4)
