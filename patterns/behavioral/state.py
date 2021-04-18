"""
State

Allows and object to alter its behaviour when its internal state changes.
It appears as if the object has changed class.
"""


from typing import Protocol


class PState(Protocol):

    def handle(self, context: PContext, msg: str) -> None: ...

    def write_name(self, name: str) -> None: ...



class PContext(Protocol):

    # update state by handling a msg
    def handle(self, msg: str) -> None: ...

    def set_state(self, msg: str) -> None: ...

    def write_name(self, name: str) -> None: ...


class Context(PContext):

    def __init__(self, initial_state: PState):
        self._state: PState = initial_state

    def handle(self, msg: str) -> None:
        self._state.handle(context=self, msg=msg)

    def set_state(self, state: PState) -> None:
        self._state = state

    def write_name(self, name: str) -> None:
        self._state.write_name(name=name)


class StateOne(PState):

    """Capitalise"""

    def handle(self, context: PContext, msg: str) -> None:
        if msg:
            context.set_state(StateTwo())

    def write_name(self, name: str) -> None:
        print(name.upper())


class StateTwo(PState):

    """Lower"""

    def handle(self, context: PContext, msg: str) -> None:
        if 'event' in msg:
            context.set_state(StateOne())

    def write_name(self, name: str) -> None:
        print(name.lower())
