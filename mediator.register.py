from typing import Protocol, Set


class PMediator(Protocol):

    def notify(self, msg: str) -> None: ...
    """notify the mediator"""

    def register(self, component: 'BaseComponent') -> None: ...
    """register a component with the mediator"""


class BaseComponent:

    def __init__(self, name: str, mediator: PMediator = None):
        self.name: str = name
        self.mediator: PMediator = mediator

    def handle(self, msg: str) -> None:
        """handle a msg sent from the mediator"""
        print(f'{self.name} handled msg: {msg}')

    def notify(self, msg: str) -> None:
        """notify the mediator of a msg"""
        self.mediator.notify(msg)


class Mediator(PMediator):

    def __init__(self):
        self.components: Set[BaseComponent] = set()

    def register(self, component: BaseComponent):
        component.mediator = self
        self.components.add(component)

    def notify(self, msg: str) -> None:
        """notify the components by pushing the msg to handle"""
        for component in self.components:
            component.handle(msg)


def main():
    components = [
        BaseComponent(f'component {letter}')
        for letter
        in ('A', 'B', 'C')
    ]

    mediator = Mediator()
    for component in components: mediator.register(component)

    component_a, *rest = components
    component_a.notify(msg='Hello from A')


if __name__ == '__main__':
    main()
