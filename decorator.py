"""
Decorator

Attach additional responsibilities to an object dynamically.

Applicability
    - add responsibilities to objects dynamically and transparently
    - for responsibilities that can be withdrawn
    - when subclass is impractical
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
        '''Decorator over opteration'''
        return f'Concrete Decorator A decorating {self._component.operation()}'

    def addition_behavior(self) -> str:
        return 'Some decorator A additional behaviour'


def main() -> None:
    component = ConcreteComponent()
    print(component.operation())

    decorated_component = ConcreteDecoratorA(component=ConcreteComponent())
    print(decorated_component.operation())
    print(decorated_component.addition_behavior())


if __name__ == '__main__':
    main()
