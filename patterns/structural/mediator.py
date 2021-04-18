from typing import Protocol


class PMediator(Protocol):

    def notify(self, sender: object, event: str) -> None: ...


class BaseComponent:

    def __init__(self, mediator: PMediator = None) -> None:
        self.mediator: PMediator = mediator


class ComponentOne(BaseComponent):

    def do_a(self) -> None:
        print("Component One does A.")
        self.mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component One does B.")
        self.mediator.notify(self, "B")


class ComponentTwo(BaseComponent):

    def do_c(self) -> None:
        print("Component Two does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component Two does D.")
        self.mediator.notify(self, "D")


class ConcreteMediator(PMediator):

    def __init__(self, component_one: ComponentOne, component_two: ComponentTwo) -> None:
        self._component_one: ComponentOne = component_one
        self._component_one.mediator = self
        self._component_two: ComponentTwo = component_two
        self._component_two.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == 'A':
            print('ConcreteMediator reacts on A and triggers the following operations')
            self._component_two.do_c()
        if event == 'D':
            print('ConcreteMediator reacts on A and triggers the following operations')
            self._component_one.do_b()
            self._component_two.do_c()


def main():
    c1 = ComponentOne()
    c2 = ComponentTwo()
    mediator = ConcreteMediator(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()


if __name__ == "__main__":
    main()
