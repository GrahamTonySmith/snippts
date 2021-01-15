"""
Decorator

A compnent implements some interface I
A base decorator which decorates the compnent implements the same interface I
A concrete decorator inherets from the base decorator
"""

from typing import Protocol



class PComponent(Protocol):

    def operation(self) -> str: ...


class ConcreteComponent(PComponent):

    def operation(self) -> str:
        return 'Concrete Component'


class BaseDecorator(PComponent):

    _component: PComponent

    def __init__(self, component: PComponent) -> None:
        self._component = component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(BaseDecorator):

    def operation(self) -> str:
        return f'Concrete Decorator A decorating {self._component.operation()}'

    def addition_operation(self) -> str:
        return 'Some A specific operation'


def main() -> None:
    component = ConcreteComponent()
    print(component.operation())

    decorated = ConcreteDecoratorA(component=ConcreteComponent())
    print(decorated.operation())


if __name__ == '__main__':
    main()
