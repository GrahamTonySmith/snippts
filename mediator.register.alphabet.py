from typing import Protocol, Set, Dict, Iterable
from collections import defaultdict


class PEvent(Protocol):

    name: str


class GenericEventHappened(PEvent):

    name = 'generic_event'


class CandleClosed(PEvent):

    name = 'candle_closed'


class SignalFound(PEvent):

    name = 'signal_found'


class PMediator(Protocol):

    def notify(self, event: PEvent) -> None: ...
    """notify the mediator"""

    def register(self, component) -> None: ...
    """register a component with the mediator"""


class BaseComponent:

    alphabet: Iterable[str] = ()

    def __init__(self, name: str, mediator: PMediator = None):
        self.name: str = name
        self.mediator: PMediator = mediator  # runner?

    def handle(self, event: PEvent):
        print(self.name + ' handled: ' + event.name)

    def notify(self, event: PEvent):
        self.mediator.notify(event=event)


class ComponentOne(BaseComponent):

    alphabet: Iterable[str] = (CandleClosed.name, GenericEventHappened.name)


class ComponentTwo(BaseComponent):

    alphabet: Iterable[str] = (CandleClosed.name, SignalFound.name)


class Mediator(PMediator):

    def __init__(self):
        # mapping of event to component
        self.mappings: Dict[str, Set[BaseComponent]] = defaultdict(set)

    def register(self, component: BaseComponent):
        component.mediator = self
        for event_name in component.alphabet:
            self.mappings[event_name].add(component)

    def notify(self, event: PEvent):
        for component in self.mappings.get(event.name):
            component.handle(event)


def main():

    mediator = Mediator()

    component_one = ComponentOne(name='component_one')
    component_two = ComponentTwo(name='component_two')

    mediator.register(component_one)
    mediator.register(component_two)

    event_happened = GenericEventHappened()
    event_signal = SignalFound()
    event_candle = CandleClosed()

    mediator.notify(event=event_happened)
    mediator.notify(event=event_signal)
    mediator.notify(event=event_candle)


if __name__ == '__main__':
    main()
